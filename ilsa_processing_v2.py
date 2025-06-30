from pathlib import Path
import pandas as pd
import numpy as np
from scipy import signal as sig
from pydub import AudioSegment

# ---- Physical / instrument constants -----------------------------
BETA = 60e-6    # m/s² per K, linear drift coeff (ICARUS Fig 6)

# ---- Signal processing params ------------------------------------
HP, LP   = 2, 60        # Hz band‑pass, widen upper cut-off
STA_WIN  = 0.5          # s
LTA_WIN  = 5.0         # s, shorter windows to catch bursty HF energy
TRIG_TH  = 2.5          # STA/LTA ratio
MERGE_GAP= 5.0          # s

# ---- Audio params -------------------------------------------------
FS_AUDIO = 44_100
SPEEDUP  = 50           # × time‑compression (4 s → 0.08 s)
EVENT_SEC= 4.0          # window before compression
CROSS_MS = 50
TOP_N_UNKNOWN = 5


def butter_band(x, fs, hp=HP, lp=LP, order=4):
    nyq = fs/2
    lp_e = min(lp, nyq*0.9)
    hp_e = min(hp, lp_e*0.8)
    if lp_e<=0 or hp_e>=nyq:
        return x
    b,a = sig.butter(order, [hp_e/nyq, lp_e/nyq], 'band')
    return sig.filtfilt(b,a,x)

def to_audio(x, fs_in):
    if x.size==0 or np.isnan(x).all():
        raise ValueError
    resamp = sig.resample(x, int(len(x)*FS_AUDIO/fs_in/SPEEDUP))
    resamp = resamp/np.max(np.abs(resamp))
    pcm16 = (resamp*32767).astype(np.int16).tobytes()
    return AudioSegment(pcm16, frame_rate=FS_AUDIO, sample_width=2, channels=1)

def safe_append(a, b, cross=CROSS_MS):
    cf = min(cross, len(a)//2, len(b)//2)
    return a.append(b, crossfade=cf)

def process_csv(csv_path):
    try:
        df = pd.read_csv(csv_path)
    except Exception:
        return []

    time_col = df.get('Time', df.get('UTC'))
    if time_col is None:
        return []

    fine_cols = {'X Fine Acceleration','Y Fine Acceleration','Z Fine Acceleration'}
    mode = 'fine' if fine_cols.issubset(df.columns) else 'coarse'
    fs = 200 if mode=='fine' else 90

    ax = df[f'X {mode.capitalize()} Acceleration'].to_numpy()
    ay = df[f'Y {mode.capitalize()} Acceleration'].to_numpy()
    az = df[f'Z {mode.capitalize()} Acceleration'].to_numpy()

    # temperature drift correction (linear)
    if 'Temperature' in df.columns:
        temp = df['Temperature'].to_numpy()
        drift = BETA*(temp-temp.mean())
        ax -= drift; ay -= drift; az -= drift

    # tilt removal if coarse present and we're in fine mode
    if mode=='fine' and 'X Coarse Acceleration' in df.columns:
        gvec = df[['X Coarse Acceleration','Y Coarse Acceleration','Z Coarse Acceleration']].median().to_numpy()
        ax-=gvec[0]; ay-=gvec[1]; az-=gvec[2]

    ax_f = butter_band(ax,fs); ay_f=butter_band(ay,fs); az_f=butter_band(az,fs)
    vec = np.sqrt(ax_f**2+ay_f**2+az_f**2)

    # STA/LTA detector
    sta_n = int(STA_WIN*fs)
    lta_n = int(LTA_WIN*fs)
    if lta_n<=sta_n:
        lta_n = sta_n*2
    sta = sig.lfilter(np.ones(sta_n)/sta_n,1,vec)
    lta = sig.lfilter(np.ones(lta_n)/lta_n,1,vec)
    ratio = np.where(lta>0, sta/lta,0)
    trig_idx = np.flatnonzero(ratio>TRIG_TH)
    if trig_idx.size==0:
        return []
    groups = np.split(trig_idx, np.where(np.diff(trig_idx) > MERGE_GAP*fs)[0]+1)
    events=[]
    win = int(EVENT_SEC*fs/2)
    for g in groups:
        s,e = g[0], g[-1]
        peak = np.max(np.abs(az_f[s:e+1]))
        if peak>0.1:   # m/s² guard
            continue
        mid = (s+e)//2
        seg = slice(max(mid-win,0), min(mid+win,len(az_f)))
        try:
            clip = to_audio(az_f[seg], fs)
        except ValueError:
            continue
        events.append({
            'csv': Path(csv_path).name,
            'sensor_mode': mode,
            'utc_start': time_col.iloc[s],
            'utc_end':   time_col.iloc[e],
            'peak_g':    peak,
            'waveform_z': az_f[seg],
            'clip':      clip,
            'fs':        fs,
        })
    return events 