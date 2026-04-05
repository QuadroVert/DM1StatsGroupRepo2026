import numpy as np
import pandas as pd
from scipy import interpolate, integrate
import os
import matplotlib
import matplotlib.pyplot as plt

#Note, turn this into a function so it doesn't always display it all
# basic function
def load_xenon1t_data(csv_directory='SourceData', filenames=None):
    """
    Loads XENON1T CSV files into a dictionary of pandas DataFrames.

    Args:
        csv_directory (str): The directory where the CSV files are located.
        filenames: A list of CSV filenames to load.

    Returns:
        dict: A dictionary where keys are filenames and values are pandas DataFrames.
    """
    if filenames is None:
        filenames = [
            's2_response_nr.csv',
            's2_response_er.csv',
            's2_response_n_produced_electrons.csv',
            's2_binning_info.csv',
            'events_after_cuts.csv',
            'events_after_cuts_training.csv',
            'er_and_cevns_background.csv'
        ]

    dataframes = {}
    
    for filename in filenames:
        filepath = os.path.join(csv_directory, filename)
        dataframes[filename] = pd.read_csv(filepath)

    return dataframes 