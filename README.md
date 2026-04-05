# DM1 Stats Group Project — XENON1T S2-Only Analysis

Group Project DM1 for the Statistics for Modern Physics (BSc) course. 

Replication and statistical analysis of the XENON1T S2-only dark matter search, built specifically from the S2only_data_release. 

---

## Repository Structure

The repository is structured as specified in the report (folders data/, src/, notebooks/, plots/) with some tweaks. Mainly, data/ is now SourceData to reflect the nature of the original data, and tests/ showcased early test files checking out initial python loaders. 
NOTE: ReportDM12026.pdf is the report itself. 

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
| `likelihood.ipynb` | Implements the binned Poisson log-likelihood for the background normalisation β, first over the full S2 range then restricted to the ROI (165.3–271.7 PE). Finds β̂ via MLE and quantifies the frequentist uncertainty from the log-likelihood curvature (β̂ = 7.59 ± 1.90). The last part showcases how mu_s impacts, though the mu_s chosen was arbitrary, and is meant moreseo to showcase the peak. 
| `Signal_test.ipynb` | Defines the joint likelihood L(data \| µ_s, β). Computes the Bayes factor B₀₁ under flat and scale-invariant (1/µ_s) priors and discusses prior sensitivity. Also scans DM masses 3–6 GeV/c² to produce the 90% CL upper limit curve on the SI DM–nucleon cross section, reproducing Fig. 5(a) of the XENON1T paper. |
| `background_comparison.ipynb` | Overlays all three background inference approaches on a single axis: the frequentist Laplace approximation (±1σ from log-likelihood curvature) from 'likelihood.ipynb' and the two Bayesian posteriors (flat and scale-invariant priors) from `Background_fit.ipynb`. Produces `plots/frequentist_vs_bayesian_density.png`. This is the core part of our report. 

All notebooks import shared variables (binning, observed counts, background model, signal template, ROI) from `src/loader.py`.

The `plots/` directory contains all generated figures (background fits, log-likelihood scans, posteriors, upper limit curves).

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