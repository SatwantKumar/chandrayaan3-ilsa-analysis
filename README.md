# Chandrayaan-3 ILSA: End-to-End Analysis & Sonification

**Author:** Dr. Satwant Kumar  
**Date:** January 2025  
**Version:** 2.0 (Scientifically Vetted)

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Data](https://img.shields.io/badge/Data-ISRO-orange)](https://pradan.issdc.gov.in/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)](https://jupyter.org/)

---

## 🌙 Mission Overview

This repository contains a comprehensive analysis of seismic data collected by the **Instrument for Lunar Seismic Activity (ILSA)** aboard India's Chandrayaan-3 mission. ILSA represents humanity's first seismometer to operate on the lunar surface since the Apollo missions, providing unprecedented insights into lunar seismic activity.

### 🏆 Key Achievements

- **📊 Complete analysis of 4,994 seismic events** detected over 11.4 days of operation
- **🎵 Audio sonification** of lunar seismic activity for public engagement  
- **📈 Scientific validation** of significant events from John et. al., ICARUS 2024 publication
- **🔬 Multi-method spectral analysis** with statistical validation
- **📋 Open dataset** with comprehensive event catalog and metadata

---

## 📚 References & Citations

1. **Chandrayaan-3 Mission:** Indian Space Research Organisation (ISRO). Chandrayaan-3 Mission. https://www.isro.gov.in/Chandrayaan3_Details.html

2. **ILSA Instrument:** John, J., et al. (2024). "Identification and preliminary characterisation of signals recorded by instrument for lunar seismic activity at the Chandrayaan 3 landing site." *Icarus*, 424, 116285. https://doi.org/10.1016/j.icarus.2024.116285

3. **Data Archive:** Chandrayaan-3 ILSA Data. ISRO PRADAN. https://pradan.issdc.gov.in/

---

## 🛠️ Technical Implementation

This analysis implements **scientifically vetted processing** with the following key features:

✅ **True sampling rates:** 200 Hz (fine mode), 90 Hz (coarse mode)  
✅ **Temperature drift correction:** β = 60 µg K⁻¹ (validated against ICARUS Fig 6)  
✅ **Peak-g filtering:** Exclude |g| > 0.1 m s⁻² (outside fine sensor specifications)  
✅ **Enhanced sonification:** 4-second windows with 50× speed-up for audible output  
✅ **Parallel processing:** Multi-core analysis for computational efficiency

---

## 📂 Repository Structure

```
chandrayaan3-ilsa-analysis/
├── README.md                           # This file
├── LICENSE                             # MIT License
├── requirements.txt                    # Python dependencies
├── ILSA_full_analysis_v2.ipynb        # Main analysis notebook
├── ilsa_processing_v2.py              # Core processing module
├── data/                               # Data directory structure
│   └── README_data.md                  # Data acquisition instructions
├── outputs/                            # Generated outputs
│   ├── media/                          # Audio files
│   ├── visualizations/                 # Plots and figures
│   └── catalogs/                       # Event catalogs
├── docs/                               # Additional documentation
│   ├── ILSA_DataUserManual.pdf        # Data user manual
│   └── methodology.md                  # Processing methodology
└── examples/                           # Usage examples
    └── quickstart.ipynb               # Getting started guide
```

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+**
- **Jupyter Notebook** or **JupyterLab**
- **ILSA Calibrated Dataset** (see [Data Access](#-data-access))

### Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/satwantkumar/chandrayaan3-ilsa-analysis.git
   cd chandrayaan3-ilsa-analysis
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv ilsa_env
   source ilsa_env/bin/activate  # On Windows: ilsa_env\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up data directory:**
   - Follow instructions in `data/README_data.md` to obtain ILSA dataset
   - Ensure data structure matches the expected format

5. **Launch Jupyter:**
   ```bash
   jupyter notebook ILSA_full_analysis_v2.ipynb
   ```

---

## 📊 Dataset Description

### 🛰️ ILSA Data Characteristics

The **Instrument for Lunar Seismic Activity (ILSA)** collected continuous three-axis acceleration data during Chandrayaan-3's operational period on the lunar surface from August 24 to September 4, 2023.

#### **📊 Data Specifications:**
- **📅 Collection Period:** August 24 - September 4, 2023 (11.4 days)
- **📡 Sampling Rates:** 
  - **Fine Mode:** 200 Hz (high precision, short duration)
  - **Coarse Mode:** 90 Hz (lower precision, continuous operation)
- **🔧 Sensor Range:** ±2 g (fine), ±20 g (coarse)
- **🌡️ Temperature Range:** Operated through lunar day/night cycles (-180°C to +120°C)
- **📍 Location:** Chandrayaan-3 Landing Site (69.37°S, 32.32°E)

#### **📁 Expected Data Structure:**
```
ils/data/calibrated/
├── 20230824/               # Daily folders
│   ├── ch3_ils_*_accln.csv # Calibrated acceleration files
│   └── ch3_ils_*_accln.xml # Metadata files
├── 20230825/
└── ... (continuing through 20230904)
```

---

## 📈 Analysis Pipeline

### 1️⃣ **Data Processing**
- **Automated CSV file discovery** across all daily folders
- **Parallel processing** using ProcessPoolExecutor for efficiency
- **Quality filtering** with peak-g guards and sensor mode detection
- **Temperature drift correction** using scientifically validated coefficients

### 2️⃣ **Event Detection**
- **Multi-threshold detection** algorithms
- **Signal-to-noise ratio** analysis
- **Event windowing** with optimal time segments
- **Metadata extraction** with complete provenance tracking

### 3️⃣ **Audio Sonification**
- **Frequency shifting** to audible range (50× speed-up)
- **Amplitude normalization** for consistent playback
- **Montage creation** for both individual events and collections
- **Format optimization** for various playback devices

### 4️⃣ **Scientific Validation**
- **Multi-method spectral analysis:** Welch, Multitaper, and FFT validation
- **Statistical significance testing:** 2σ threshold with confidence intervals
- **STA/LTA event validation:** Short-term/Long-term average ratio analysis
- **Cross-referencing** with published ICARUS 2024 events

### 5️⃣ **Visualization & Output**
- **Time-frequency analysis** with publication-quality plots
- **Chronological heatmaps** showing temporal distribution
- **Event catalogs** in multiple formats (CSV, JSON)
- **Audio outputs** in WAV format for sonification

---

## 🎵 Audio Outputs

The analysis generates several types of audio files:

### **🏆 Top Events Montage**
- `moonbeat_montage_v2.wav` - Highest amplitude events
- Short, focused listening experience

### **🌍 Complete Collection**
- `moonbeat_all_4994_events.wav` - All detected events
- ~3.2 minutes of complete lunar seismic activity

### **📋 TABLE1 Events**
- Individual clips for scientifically significant events
- Validated against ICARUS 2024 publication
- Separate files for classified vs. unknown events

---

## 📊 Key Results

### **🔢 Detection Statistics:**
- **📈 Total Events Detected:** 4,994 seismic events over 11.4 days
- **⏱️ Average Event Rate:** 438.5 events per day (18.2 events per hour)
- **📅 Peak Activity:** September 1, 2023 (807 events in one day)
- **🏔️ Magnitude Range:** 1.64×10⁻¹⁴ to 9.96×10⁻² m/s²

### **🔬 Scientific Validation:**
- **✅ ICARUS 2024 Events:** 5/9 events successfully validated (55.6%)
- **📊 Multi-method Analysis:** Consensus validation across three spectral methods
- **🎯 Quality Metrics:** Average quality score of 0.649
- **📈 Confidence Level:** High-confidence matches with statistical significance

---

## 🔬 Scientific Methodology

### **Processing Pipeline Features:**

#### **✅ Instrument Calibration:**
- True sampling rates with automatic mode detection
- Sensor range validation and quality checks

#### **✅ Environmental Corrections:**  
- Linear temperature drift removal using β = 60 µg K⁻¹ coefficient
- Based on laboratory calibration data (ICARUS 2024, Figure 6)

#### **✅ Quality Filtering:**
- Peak-g guard excluding events with |g| > 0.1 m s⁻²
- Data reliability within instrument operating range

#### **✅ Advanced Signal Processing:**
- Butterworth bandpass filtering with optimal frequency ranges
- Multi-window spectral analysis for robust detection
- Adaptive thresholding based on local noise characteristics

#### **✅ Statistical Validation:**
- 2σ significance testing with confidence intervals
- Consensus requirement across multiple spectral methods
- STA/LTA validation with optimized time windows

---

## 💻 Usage Examples

### **Basic Analysis:**
```python
from ilsa_processing_v2 import process_csv
from pathlib import Path

# Process single CSV file
csv_file = Path('ils/data/calibrated/20230824/ch3_ils_*.csv')
events = process_csv(csv_file)

# Display results
print(f"Found {len(events)} events")
```

### **Batch Processing:**
```python
from concurrent.futures import ProcessPoolExecutor
import pandas as pd

# Process all CSV files in parallel
csv_files = sorted(Path('ils/data/calibrated').glob('**/*_accln.csv'))
all_events = []

with ProcessPoolExecutor(max_workers=8) as executor:
    futures = {executor.submit(process_csv, f): f for f in csv_files}
    for future in as_completed(futures):
        all_events.extend(future.result())

# Create event catalog
catalog_df = pd.DataFrame(all_events)
```

### **Audio Generation:**
```python
from pydub import AudioSegment, effects

# Create audio montage
montage = events[0]['clip']
for event in events[1:10]:  # First 10 events
    montage = safe_append(montage, event['clip'])

# Export audio file
montage = effects.normalize(montage)
montage.export('lunar_events.wav', format='wav')
```

---

## 📖 Documentation

### **Core Files:**
- `ILSA_full_analysis_v2.ipynb` - Complete analysis workflow
- `ilsa_processing_v2.py` - Core processing functions
- `docs/methodology.md` - Detailed scientific methodology
- `docs/ILSA_DataUserManual.pdf` - Official ISRO data manual

### **Output Files:**
- Event catalogs in `outputs/catalogs/`
- Audio files in `outputs/media/`
- Visualizations in `outputs/visualizations/`

---

## 🌐 Data Access

### **Primary Sources:**
- **ISRO PRADAN:** https://pradan.issdc.gov.in/
- **Official Documentation:** ILSA Data Users Manual (included)

### **Data Requirements:**
1. **Calibrated acceleration data** in CSV format
2. **Proper directory structure** (see Dataset Description)
3. **Complete time series** for accurate event detection
4. **Metadata files** for validation and provenance

### **⚠️ Important Notes:**
- This analysis uses **pre-calibrated data** with instrument corrections applied
- **Temperature effects** are corrected using laboratory-validated coefficients
- **Quality flags** help identify periods with potential data issues
- All **timestamps are in UTC**
- **Coordinate system:** X=East, Y=North, Z=Up (lunar surface-fixed frame)

---

## 🤝 Contributing

We welcome contributions from the scientific community! Please:

1. **Fork the repository**
2. **Create feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit changes** (`git commit -m 'Add AmazingFeature'`)
4. **Push to branch** (`git push origin feature/AmazingFeature`)
5. **Open Pull Request**

### **Areas for Contribution:**
- **Algorithm improvements** for event detection
- **Additional visualization** methods
- **Performance optimizations** for large datasets
- **Educational materials** and tutorials
- **Integration** with other planetary seismology datasets

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

This analysis builds upon the outstanding work of:

- **ISRO Chandrayaan-3 Team** for successful mission execution
- **ILSA Instrument Team** for providing high-quality calibrated data  
- **Dr. J. John and colleagues** for the foundational ICARUS 2024 publication
---

## 📞 Contact & Support

- **Issues:** Please use GitHub Issues for bug reports and feature requests
- **Discussions:** Use GitHub Discussions for questions and community interaction
- **Email:** MyFirstName.Dagar@[G-M-A I-L]

---

## 🌟 Citation

If you use this code or analysis in your research, please cite:

```bibtex
@software{kumar2025_ilsa_analysis,
  author = {Kumar, Satwant},
  title = {Chandrayaan-3 ILSA: End-to-End Analysis \& Sonification},
  year = {2025},
  url = {https://github.com/satwantkumar/chandrayaan3-ilsa-analysis},
  version = {2.0}
}
```

And the original ILSA paper:
```bibtex
@article{john2024ilsa,
  title={Identification and preliminary characterisation of signals recorded by instrument for lunar seismic activity at the Chandrayaan 3 landing site},
  author={John, J. and others},
  journal={Icarus},
  volume={424},
  pages={116285},
  year={2024},
  publisher={Elsevier}
}
```

---

*"Through ILSA's sensitive ears, we have listened to the Moon's heartbeat and made it audible to humanity."*

**🌙 End of Documentation 🌙** 
