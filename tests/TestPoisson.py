from Testloader import load_xenon1t_data

#Basic import test, general idea is to import loader in each file we use for different charts.
# For now it should just again print out the loaded csv files, will change later.

# changed, actually works for a quick test of loading

dataframes = load_xenon1t_data()

bins = dataframes['s2_binning_info.csv']
resp_nr = dataframes['s2_response_nr.csv']
resp_er = dataframes['s2_response_er.csv']
bg = dataframes['er_and_cevns_background.csv']
events = dataframes['events_after_cuts.csv']