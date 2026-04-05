import numpy as np
import pandas as pd
import wimprates as wr

# NOTE, this was originally in likelihood.ipynb as at first it was assumed to have been
# the only file we'd work in. But, more changes and different approaches then lead to the
# creation of new files, so it necessitated again a proper loader function.

bins    = pd.read_csv('SourceData/s2_binning_info.csv')
resp_nr = pd.read_csv('SourceData/s2_response_nr.csv')
resp_er = pd.read_csv('SourceData/s2_response_er.csv')
bg      = pd.read_csv('SourceData/er_and_cevns_background.csv')
events  = pd.read_csv('SourceData/events_after_cuts.csv')

#Extract binning information
s2_bin_centers_log = bins['log_center_pe'].values
s2_bin_centers_lin = bins['linear_center_pe'].values
s2_bin_widths      = (bins['end_pe'] - bins['start_pe']).values
s2_bin_edges       = np.concatenate([bins['start_pe'].values, [bins['end_pe'].iloc[-1]]]) #start_pe contains all the edges except the last one, which we add with bins['end_pe'].iloc[-1]

#The authors of the paper made a cut on the data and what survived are the potential events(which still may include background noise).
#This is what we extract below
k_obs, _ = np.histogram(events['s2_area_pe'].values, bins=s2_bin_edges) #np.histogram returns counts, bin_edges, but we only care about the counts.
#k_obs[j] is the number of observed events in S2 bin j
#the s2_area_pe is the amount of photoelectron counts per S2 interval(height x width = Area); they only care about events with S2 area between 90 and 3000PE
#that's where the cut comes from.

b_er      = bg['er_background_events']
b_cevns   = bg['cevns_background_events']
b_nominal = b_er + b_cevns

#Extracting information from nuclear recoil response
s2_energies        = resp_nr['energy_kev'].values
bin_starts         = resp_nr['energy_bin_start_kev'].values
bin_ends           = resp_nr['energy_bin_end_kev'].values
dE                 = bin_ends - bin_starts
response_matrix_nr = resp_nr.values[:, 3:] #we start from the 4th column, since the 3 previous ones are energies. The 4th column is s2_bin_000.

reference_cross_section = 1e-45  # cm²

#Most of the code below was copied directly from the Public Data Release
rate_pertonneyear = wr.rate_wimp_std(es=s2_energies, mw=4, sigma_nucleon=reference_cross_section) * dE
rate_before_cutoff = rate_pertonneyear * 0.97678
#The authors of the paper remove events below 0.7keV
recoil_energy_cutoff_kev = 0.7
rate_after_cutoff = rate_before_cutoff.copy()

# Which bin contains the cutoff?
cutoff_bin_index = (bin_starts < recoil_energy_cutoff_kev).sum() - 1 #This counts how many bins start below 0.7 keV, then subtracts 1 to get the index

# All bins fully below 0.7 keV are removed
rate_after_cutoff[:cutoff_bin_index] = 0

# Suppress the spectrum proportionally in the bin with the cutoff
suppress_by = (
    (recoil_energy_cutoff_kev - bin_starts[cutoff_bin_index])
    / bin_starts[cutoff_bin_index])
assert 0 <= suppress_by <= 1

#Only keep the part above the cutoff
rate_after_cutoff[cutoff_bin_index] *= 1 - suppress_by

s_i = rate_after_cutoff @ response_matrix_nr

# ROI (explained in likelihood.ipynb)
ROI      = (165.3, 271.7)  # PE (log-center)
roi_mask = (s2_bin_centers_log >= ROI[0]) & (s2_bin_centers_log <= ROI[1])
