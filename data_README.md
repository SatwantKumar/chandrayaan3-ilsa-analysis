# ILSA Dataset Setup Guide

This document provides instructions for obtaining and setting up the Chandrayaan-3 ILSA dataset for analysis.

## 📂 Required Data Structure

The analysis expects the following directory structure:

```
ils/data/calibrated/
├── 20230824/
│   ├── ch3_ils_nop_calib_20230824t101208872_d_accln.csv
│   ├── ch3_ils_nop_calib_20230824t101208872_d_accln.xml
│   ├── ch3_ils_nop_calib_20230824t104208888_d_accln.csv
│   ├── ch3_ils_nop_calib_20230824t104208888_d_accln.xml
│   └── ... (more files)
├── 20230825/
│   ├── ch3_ils_nop_calib_20230825t120121952_d_accln.csv
│   ├── ch3_ils_nop_calib_20230825t120121952_d_accln.xml
│   └── ... (more files)
├── 20230826/
├── 20230827/
├── 20230828/
├── 20230829/
├── 20230830/
├── 20230831/
├── 20230901/
├── 20230902/
├── 20230903/
└── 20230904/
```

## 🌐 Data Sources

### Primary Source: ISRO PRADAN
- **URL:** https://pradan.issdc.gov.in/
- **Dataset:** Chandrayaan-3 ILSA Calibrated Data
- **Registration:** Required for access
- **Format:** ZIP archives containing daily folders

### Alternative Sources
- Contact ISRO directly for academic/research access
- Check NASA PDS (Planetary Data System) for archived copies
- Collaborate with institutions that have existing access

## 📋 File Specifications

### CSV Files
- **Naming Convention:** `ch3_ils_nop_calib_YYYYMMDDtHHMMSSsss_d_accln.csv`
- **Content:** Time series acceleration data
- **Columns:**
  - `Time`: UTC timestamp
  - `X Fine Acceleration`: High-precision X-axis (m/s²)
  - `Y Fine Acceleration`: High-precision Y-axis (m/s²)
  - `Z Fine Acceleration`: High-precision Z-axis (m/s²)
  - `X Coarse Acceleration`: Lower-precision X-axis (m/s²)
  - `Y Coarse Acceleration`: Lower-precision Y-axis (m/s²)
  - `Z Coarse Acceleration`: Lower-precision Z-axis (m/s²)
  - `Temperature`: Instrument temperature (°C)

### XML Files
- **Naming Convention:** `ch3_ils_nop_calib_YYYYMMDDtHHMMSSsss_d_accln.xml`
- **Content:** Metadata and processing parameters
- **Purpose:** Validation and provenance tracking

## 🔧 Setup Instructions

### 1. Download Data
1. Register at ISRO PRADAN portal
2. Navigate to Chandrayaan-3 → ILSA → Calibrated Data
3. Download daily ZIP files for August 24 - September 4, 2023
4. Extract to maintain the folder structure shown above

### 2. Verify Data Integrity
```bash
# Check total file count (should be ~646 CSV files)
find ils/data/calibrated -name "*.csv" | wc -l

# Check date range
ls ils/data/calibrated/
```

### 3. Test Data Access
```python
from pathlib import Path
import pandas as pd

# Test loading a sample file
csv_files = list(Path('ils/data/calibrated').glob('**/*_accln.csv'))
print(f"Found {len(csv_files)} CSV files")

# Load first file to verify format
if csv_files:
    df = pd.read_csv(csv_files[0])
    print(f"Sample file shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
```

## ⚠️ Important Notes

### Data Size
- **Total Size:** ~15-20 GB uncompressed
- **Files:** ~1,300 files (646 CSV + 646 XML)
- **Time Span:** 11.4 days of continuous data

### Processing Requirements
- **RAM:** Minimum 8 GB recommended for parallel processing
- **Storage:** Additional 5-10 GB for outputs and temporary files
- **CPU:** Multi-core processor recommended for efficient analysis

### Data Quality
- Some files may have gaps due to operational constraints
- Temperature extremes during lunar night may affect data quality
- Fine mode data has higher precision but shorter duration
- Coarse mode provides continuous coverage with lower resolution

### Privacy & Usage
- **Academic Use:** Generally permitted with proper attribution
- **Commercial Use:** May require additional permissions
- **Data Sharing:** Follow ISRO guidelines for redistribution
- **Citation:** Always cite original ISRO/ILSA team publications

## 🆘 Troubleshooting

### Common Issues

#### "File not found" errors
- Verify directory structure matches expected format
- Check file permissions
- Ensure all ZIP files were properly extracted

#### "Permission denied" errors
```bash
# Fix file permissions if needed
chmod -R 755 ils/data/calibrated/
```

#### Large memory usage
- Reduce parallel workers in configuration
- Process data in smaller batches
- Monitor system resources during analysis

#### Missing dependencies
```bash
# Install required packages for audio processing
# On Ubuntu/Debian:
sudo apt-get install ffmpeg

# On macOS:
brew install ffmpeg
```

## 📞 Support

- **Technical Issues:** Check the main repository issues
- **Data Access:** Contact ISRO PRADAN support
- **Scientific Questions:** Refer to ILSA publications and documentation

## 📚 Additional Resources

- **ILSA Data User Manual:** `docs/ILSA_DataUserManual.pdf`
- **ICARUS 2024 Paper:** DOI: 10.1016/j.icarus.2024.116285
- **Chandrayaan-3 Mission:** https://www.isro.gov.in/Chandrayaan3_Details.html

---

**Note:** This repository does not include the actual ILSA data due to size constraints. Users must obtain the data independently following the instructions above. 