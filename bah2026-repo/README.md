# 🚀 Bharatiya Antariksh Hackathon 2026

> **Event:** [Bharatiya Antariksh Hackathon 2026 by ISRO × Hack2Skill](https://hack2skill.com/event/bah2026/)

---

## 📌 Problem Statement

---

## 🗂️ Folder Structure

```
bah2026/
│
├── data/
│   ├── raw/            # Original, unmodified datasets (don't edit these)
│   ├── processed/      # Cleaned and preprocessed data
│   └── sample/         # Small sample files for quick testing
│
├── notebooks/          # Jupyter notebooks for exploration & experiments
│   └── 01_eda.ipynb    # Example: Exploratory Data Analysis
│
├── src/                # Source code (reusable Python scripts)
│   ├── preprocessing/  # Data loading, cleaning, feature engineering
│   ├── models/         # Model definitions and training scripts
│   └── utils/          # Helper functions used across the project
│
├── outputs/
│   ├── predictions/    # Model outputs and result files
│   └── visualizations/ # Charts, plots, and figures
│
├── docs/               # Documentation, references, research papers
├── tests/              # Unit tests for your code
├── scripts/            # One-off scripts (setup, download data, etc.)
│
├── .gitignore          # Files Git should ignore
├── requirements.txt    # Python dependencies
└── README.md           # You are here!
```

---
# Bharatiya Antariksh Hackathon 2026 — Problem Statement Analysis


Technical categorization of all 15 problem statements 
## Problem Statements

| # | Challenge | Tech category | AI/ML sub-field | Expected outcome | Indicative tech stack |
|---|-----------|---------------|-----------------|------------------|-----------------------|
| 1 | Urban heat mitigation & cooling strategies | Geospatial / thermal remote sensing + optimization | Predictive regression + spatial optimization | UHI risk map + engine ranking cooling interventions by impact-per-cost | Python, Google Earth Engine, rasterio/GDAL, GeoPandas, XGBoost/Random Forest, spatial optimizer, Leaflet/Mapbox |
| 2 | Cloud removal & reconstruction for LISS-IV imagery | Computer vision | Generative AI (GAN / diffusion, inpainting) | Cloud-free reconstructed imagery with PSNR/SSIM + spectral fidelity | PyTorch, conditional GANs (pix2pix/SPADE) or diffusion, Sentinel-1 SAR–optical fusion |
| 3 | Surface AQI & HCHO hotspot identification | Environmental geospatial analytics | ML regression + spatial analysis | Gridded surface AQI maps + hotspot detector validated vs ground stations | Python, xarray/netCDF, TROPOMI + ERA5 + CPCB data, gradient boosting / NN regression, DBSCAN / Getis-Ord |
| 4 | Road extraction + graph criticality analysis | Computer vision + graph theory | Semantic segmentation + network analysis | Occlusion-robust road map + ranked critical links for resilience | PyTorch (U-Net/D-LinkNet), OpenStreetMap, NetworkX/graph-tool, GeoPandas |
| 5 | Digital twin of India's climate | Climate / Earth-system modeling | Physics-informed ML / spatiotemporal forecasting | Interactive twin forecasting & simulating regional climate variables | PyTorch, neural operators (FNO) or graph/transformer models, xarray, IMD/MOSDAC + reanalysis, GPU |
| 6 | Crop type, moisture stress & irrigation advisory | Agricultural remote sensing | Multimodal (optical + SAR) fusion + time-series classification | Crop-type maps, per-field stress flags, stage-aware irrigation advice | Google Earth Engine, Python, 1D-CNN/LSTM/Transformer or Random Forest, NDVI/NDWI + SAR backscatter |
| 7 | Exoplanet detection from noisy light curves | Astronomy / signal processing | Time-series classification + denoising | Transit-candidate detector with low false-positive rate on noisy curves | Python, astropy + lightkurve, Box Least Squares, 1D-CNN/transformer, GP / wavelet detrending |
| 8 | Lunar subsurface ice detection (Chandrayaan-2) | Planetary remote sensing (SAR) + path planning | SAR classification + traverse planning | Ice-probability map + safe rover traverse routes | SAR processing (circular polarization ratio), Python, ML classification, DEM/slope, A*/RRT* planning |
| 9 | Wavefront reconstruction & turbulence (SH-WFS) | Adaptive optics / signal processing | Classical reconstruction (+ optional CNN) | Faster/accurate wavefront reconstruction + turbulence stats (r₀, Cₙ²) | Python, NumPy/SciPy, Zernike & zonal reconstructors, least-squares, optional CNN, FFT analysis |
| 10 | Infrared image colorization & enhancement | Computer vision | Generative image-to-image translation | Colorized, enhanced IR validated on detection/recognition | PyTorch, pix2pix/CycleGAN or diffusion, paired IR–visible data, perceptual + SSIM losses |
| 11 | Cross-modal satellite image retrieval | Computer vision + multimodal learning | Contrastive / cross-modal representation learning | Modality-agnostic retrieval engine measured by recall@k | PyTorch, CLIP-style dual encoders (InfoNCE/triplet), FAISS, SAR + optical data |
| 12 | Temporal resolution enhancement (frame interpolation) | Computer vision (video) | Optical flow + frame synthesis | Plausible interpolated scenes between passes, validated vs held-out dates | PyTorch, optical flow (RAFT) + RIFE/FILM synthesis, warping + refinement nets |
| 13 | Air-gapped predictive copilot for MPLS operations | Networking / AIOps / secure systems | On-prem LLM + RAG + anomaly detection | Self-hosted predictive-maintenance assistant + RAG over runbooks/telemetry | Local LLMs (Llama/Mistral/Qwen), local vector DB + RAG, anomaly detection (Isolation Forest/autoencoders), air-gapped deploy |
| 14 | Radiation environment forecasting for GEO satellites | Space weather / time-series | Sequence forecasting (LSTM / Transformer) | Lead-time particle-flux forecasts with uncertainty | Python, GOES/OMNI solar-wind + Kp/Dst, LSTM/Temporal-CNN/Transformer, physics-informed features |
| 15 | Solar flare forecasting / nowcasting (Aditya-L1) | Space weather / time-series | Multimodal time-series forecasting | Flare probability/intensity nowcaster with lead time + C/M/X class | Python, X-ray time-series, dual-branch LSTM/Transformer, anomaly detection, class-imbalance handling |

## Thematic Clusters

- **EO computer vision & image generation** — 2, 4, 10, 11, 12
- **EO geospatial & environmental analytics** — 1, 3, 5, 6
- **Astronomy & space-weather time-series** — 7, 14, 15 (plus 9 as optics-flavored signal processing)
- **Planetary science** — 8
- **Networking / secure AIOps** (outlier) — 13

The computer-vision / generative cluster is the most crowded and "hackathon-default." The optics (9), planetary-SAR (8), and MPLS copilot (13) statements are the most differentiated and least likely to be over-subscribed.

## Problem Statements Explained

# 1. Urban Heat Mitigation & Cooling Strategies

Cities run hotter than their surroundings because concrete and asphalt soak up heat and radiate it back — "urban heat islands" that turn deadly in heatwaves and spike cooling-energy demand. Satellites measure ground temperature from space using thermal infrared. The job is two-fold: find a city's hottest pockets, then work out where adding trees, cool roofs, or water bodies would cool things most per rupee spent. Diagnosis plus prescription.

# 2. Cloud Removal & Reconstruction for LISS-IV Imagery

LISS-IV is a sharp optical camera on India's ResourceSat satellites (5.8 m resolution). The problem: clouds block the view and wreck images. You can't just erase cloudy pixels — you have to reconstruct the ground underneath them with generative AI (the same family behind image inpainting). The clever approach uses radar, which sees through clouds, as a guide so the AI rebuilds what's actually there rather than inventing something plausible-looking.

# 3. Surface AQI & HCHO Hotspot Identification

HCHO is formaldehyde — both a pollutant and a fingerprint for other pollution sources like vehicle exhaust, industry, and crop burning. Satellites measure how much HCHO sits in the entire vertical column of air, but what people actually breathe is the concentration at ground level. The challenge is bridging that gap: convert the satellite's column reading into a surface air-quality estimate and map the worst hotspots across India.

# 4. Road Extraction + Graph Criticality Analysis

Two parts. First, automatically trace road networks from satellite images — tricky because trees, buildings, and shadows hide stretches of road, so the model must connect the dots across gaps. Second, turn that road map into a network graph and ask which roads are critical: if a particular junction or bridge fails (flood, accident), how badly does the city fragment? Computer vision feeding into network-resilience analysis, useful for disaster planning.

# 5. Digital Twin of India's Climate

A "digital twin" is a living virtual model of a real system. Here you build an AI that emulates India's climate from national datasets, so you can run fast forecasts and "what-if" scenarios without firing up a physics supercomputer for days. It's the regional cousin of AI weather models like GraphCast that now rival traditional forecasting — the most ambitious and compute-hungry challenge on the list.

# 6. Crop Type, Moisture Stress & Irrigation Advisory

From space, you want to know: what crop is in each field, is it water-stressed, and should the farmer irrigate? Optical satellites see crop greenness but get blinded by clouds; radar (microwave) sees through clouds and senses soil moisture. This challenge fuses both, tracked across the growing season, to identify crops and give stage-aware irrigation advice. Direct impact on water management and food security.

# 7. Exoplanet Detection from Noisy Light Curves

When a planet crosses in front of its star, the star dims a tiny bit — a small periodic dip in a brightness-over-time graph called a light curve. That's how we discover planets around other stars. But the signal is buried under noise from the instrument and the star's own flickering. The challenge is building AI that reliably picks out genuine planet transits from noisy data without raising false alarms.

# 8. Lunar Subsurface Ice Detection (Chandrayaan-2)

The Moon's south pole has permanently shadowed craters that may hold water ice — hugely valuable for future bases (drinking water, rocket fuel). Chandrayaan-2's radar can probe beneath the surface, and you classify terrain into likely-ice versus not. Then you use that ice map to plan where to land and how a rover should drive to reach it safely. Remote sensing plus robotics path planning.

# 9. Wavefront Reconstruction & Turbulence (SH-WFS)

The atmosphere blurs starlight — the same reason stars twinkle. "Adaptive optics" cancels this in real time by measuring the distortion and bending a mirror to undo it. A Shack-Hartmann sensor gauges the distortion from how a grid of light spots shifts. The challenge: from that spot data over time, reconstruct the exact shape of the warped light wave and characterize the turbulence. Heavy physics and signal processing — it makes ground telescopes much sharper.

# 10. Infrared Image Colorization & Enhancement

Thermal/IR cameras see heat, not color, so their images are grayscale and hard to read. The challenge is using AI to colorize and sharpen them so objects become easier to recognize — turning a murky thermal frame into something closer to a clear color photo. An image-to-image translation problem.

# 11. Cross-Modal Satellite Image Retrieval

There are massive archives of imagery from different sensors — optical, radar, and more. Searching across them is hard: if you have a radar image of a place, can you automatically find the matching optical image, even though the two look nothing alike? You teach an AI to map different sensor "views" of the same scene into a shared space so they can be matched — essentially a search engine that recognizes a location regardless of which kind of camera captured it.

# 12. Temporal Resolution Enhancement (Frame Interpolation)

A satellite revisits the same spot only every few days, leaving gaps in time. The challenge is generating realistic "in-between" frames to fill those gaps — like video software smoothing slow-motion by inventing frames between real ones. It uses optical flow (tracking how things shift between two images) to synthesize plausible intermediate scenes, giving you effectively higher time-resolution imagery.

# 13. Air-Gapped Predictive Copilot for MPLS Operations

The odd one out — pure networking and security. MPLS is the technology that routes traffic through large telecom and enterprise networks. "Air-gapped" means it must run fully offline, no internet, for security. You build an AI assistant — a locally hosted LLM — that helps network operators predict failures, spot anomalies, and troubleshoot, with no data ever leaving the network. AIOps meets on-premise AI.

# 14. Radiation Environment Forecasting for GEO Satellites

Space is full of high-energy charged particles, and Sun-driven bursts of them can fry satellite electronics. ISRO's geostationary satellites sit right in this hazardous zone. The challenge is forecasting the radiation levels ahead of time — from solar-wind and space-weather data — so operators can shield or safe-mode satellites before a storm hits. A time-series forecasting problem with real operational stakes.

# 15. Solar Flare Forecasting / Nowcasting (Aditya-L1)

Solar flares are sudden explosions of energy on the Sun that disrupt satellites, GPS, and power grids. India's Aditya-L1 mission watches the Sun with two X-ray instruments — one for soft (lower-energy) X-rays, one for hard (higher-energy). The challenge is combining both X-ray streams to forecast or "nowcast" flares: predicting when one is coming and how strong it'll be (the C/M/X intensity classes). Time-series forecasting that fuses two energy bands.

## ⚙️ Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Vaibhav0056/bah2026.git
cd bah2026
```

### 2. Create a Virtual Environment

```bash
# Create
python -m venv venv

# Activate (Mac/Linux)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Launch Jupyter Notebook

```bash
jupyter notebook
```

Then open any notebook from the `notebooks/` folder.

---

## 🤝 Team Collaboration Guide (Read Before You Touch Anything!)

### ⚡ Golden Rules

1. **NEVER push directly to `main`**
2. **ALWAYS pull before you start working**
3. **ALWAYS work on your own branch**
4. **ALWAYS write a clear commit message**

---

### 🌿 Branch Structure

```
main        → final, working code only (no direct pushes)
dev         → combines everyone's work (merge here first)
your-name   → your personal working branch
```

---

### 🚀 Daily Workflow (Follow This Every Day)

#### 1. Before Starting Work — Always Pull First
```bash
git checkout dev          # switch to dev branch
git pull origin dev       # get latest changes from teammates
```

#### 2. Switch to Your Own Branch
```bash
git checkout your-name    # e.g. git checkout vaibhav
```
> First time only — create your branch:
> ```bash
> git checkout -b your-name
> ```

#### 3. Make Your Changes
Edit files, write code, add notebooks — do your work.

#### 4. Save & Push Your Work
```bash
git add .
git commit -m "feat: describe what you did"
git push origin your-name
```

#### 5. Merge Into Dev (When Your Work is Ready)
```bash
git checkout dev
git pull origin dev                  # pull latest dev again
git merge your-name                  # merge your branch into dev
git push origin dev                  # push merged dev to GitHub
git checkout your-name               # go back to your branch
```

---

### 🔁 End of Day Checklist

- [ ] Pushed your branch to GitHub
- [ ] Merged into `dev` if feature is complete
- [ ] Told teammates in the group chat what you changed

---

### ⚔️ How to Handle Merge Conflicts

A conflict happens when two people edit the **same line** of the same file.

Git will mark the conflict in the file like this:
```
<<<<<<< your-name
your version of the line
=======
teammate's version of the line
>>>>>>> dev
```

**To fix it:**
1. Open the file — find all `<<<<<<<` markers
2. Decide which version to keep (or combine both)
3. Delete the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
4. Save the file, then:
```bash
git add .
git commit -m "fix: resolved merge conflict in filename"
git push origin your-name
```

> 💡 **Best way to avoid conflicts:** Always pull before starting, and don't
> edit the same file as a teammate at the same time.

---

### 🚫 Never Do These

```bash
git push origin main        # ❌ never push directly to main
git push --force            # ❌ never force push (destroys teammates' work)
git commit -m "changes"     # ❌ never write vague commit messages
```

### ✅ Always Do These

```bash
git pull origin dev         # ✅ pull before starting
git status                  # ✅ check what files changed before committing
git log --oneline           # ✅ see recent commits
```

---

### 📋 Commit Message Format

```
type: short description of what you did
```

| Type | When to use |
|------|-------------|
| `feat:` | Added something new |
| `fix:` | Fixed a bug |
| `docs:` | Updated README or docs |
| `data:` | Added or changed data files |
| `refactor:` | Cleaned up code |
| `test:` | Added tests |

**Examples:**
```bash
git commit -m "feat: added cloud mask preprocessing function"
git commit -m "fix: corrected null values in dataset loader"
git commit -m "docs: added setup instructions to README"
```

---

### 🆘 Messed Something Up?

| Problem | Fix |
|---------|-----|
| Committed wrong file | `git reset HEAD~1` |
| Want to discard all local changes | `git checkout -- .` |
| Pushed to wrong branch | Tell the team lead immediately |
| Conflict you can't resolve | Don't panic — call a teammate |

---

### 📞 Before Pushing — Quick Sanity Check

```bash
git status          # see what's changed
git diff            # see exact line changes
git log --oneline   # see your recent commits
```

---

## 📓 Notebook Naming Convention

Name notebooks with a number prefix to keep them ordered:

```
01_eda.ipynb               ← Exploratory Data Analysis
02_preprocessing.ipynb     ← Data Cleaning
03_model_baseline.ipynb    ← First model attempt
04_model_improved.ipynb    ← Better version
05_results_analysis.ipynb  ← Final results
```

---

## 📦 Data

> ⚠️ **Do NOT commit large data files to Git.** Use `.gitignore` to exclude them.

- Download data from: _(add link when available)_
- Place raw files in `data/raw/`
- Use `data/sample/` for tiny test files that are okay to commit

---

## 🔗 Resources

- [Hack2Skill BAH 2026 Page](https://hack2skill.com/event/bah2026/)
- [ISRO Official Site](https://www.isro.gov.in/)
- [Mosdac Data Portal](https://www.mosdac.gov.in/) — ISRO satellite data
- [Bhuvan Portal](https://bhuvan.nrsc.gov.in/) — ISRO geo-platform
### PS7
- [AstroNet-Vetting: A Neural Network for TESS Light Curve Vetting](https://github.com/yuliang419/Astronet-Vetting)
- [Machine learning models and utilities for exoplanet science](https://github.com/google-research/exoplanet-ml)
---

## 📝 Notes & Decisions

Use this section to log important team decisions:

- [ ] Finalise problem statement
- [ ] Agree on tech stack (PyTorch / TensorFlow / sklearn)
- [ ] Set up shared data storage
- [ ] Assign roles

---

