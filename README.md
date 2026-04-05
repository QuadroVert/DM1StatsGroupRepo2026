# DM1 Stats Group Project — XENON1T S2-Only Analysis

Group Project DM1 for the Statistics for Modern Physics (BSc) course. 

Replication and statistical analysis of the XENON1T S2-only dark matter search, built specifically from the S2only_data_release. 

---

## Repository Structure

The repository is structured as specified in the report (folders data/, src/, notebooks/, plots/) with some tweaks. Mainly, data/ is now SourceData to reflect the nature of the original data, and tests/ showcased early test files checking out initial python loaders.

---

## Setup

**1. Clone the repository**
```bash
git clone https://github.com/QuadroVert/DM1StatsGroupRepo2026.git
cd DM1StatsGroupRepo2026
```

**2. Create and activate a virtual environment**
```bash
python -m venv .venv

# Windows
.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r Requirements.txt
```

---

## Running the Analysis

The notebooks can be run in any order, as each showcases separate parts.

| Notebook | Description |
|---|---|
| `Background_fit.ipynb` | Fits the background normalisation β using a Poisson likelihood. Computes the Bayesian posterior under flat and scale-invariant priors and reports the 68% credible interval. |
| `likelihood.ipynb` | Currently Implements the full binned likelihood, defines the signal region of interest (ROI: 165.3–271.7 PE). It also adds the signal component (Note: possibly should be split in separate file). |
| `Signal_test.ipynb` | Extends the likelihood to treat signal strength µ_s as a free parameter. Computes the Bayes factor B₀₁ under flat and log-uniform priors and discusses prior sensitivity. |

All notebooks import shared variables (binning, observed counts, background model, signal template, ROI) from `src/loader.py`.

---


## Data

The `SourceData/` directory contains the XENON1T public data release. For more information, go check out the readme in https://github.com/XENON1T/s2only_data_release since it is utilizing the same .csv files.

---

## Dependencies

See `Requirements.txt`. Key packages:

- `numpy`, `scipy`, `pandas`, `matplotlib`
- `wimprates` — WIMP rate calculations


## Contributors:
- Nora Andrade Hernández (S5172020)
- Ana Alonso Hernando (S6579353)
- Tudor Nicolae Vintila (S5233127)
- Maley Diaw Corral (S5048176)
- James Conlon (S5534275)