import numpy as np
import pandas as pd
from scipy import interpolate, integrate
import os
import matplotlib
import matplotlib.pyplot as plt

#Note, turn this into a function so it doesn't always display it all

# Directory of the files
csv_directory = 'SourceData'

# List of filenames to load
csv_filenames = [
    's2_response_nr.csv',
    's2_response_er.csv',
    's2_response_n_produced_electrons.csv',
    's2_binning_info.csv',
    'events_after_cuts.csv',
    'events_after_cuts_training.csv',
    'er_and_cevns_background.csv'
]

# Dictionary to store the loaded DataFrames
dataframes = {}

print(f"Attempting to load {len(csv_filenames)} files from '{csv_directory}'...")

for filename in csv_filenames:
    file_path = os.path.join(csv_directory, filename)
    df = pd.read_csv(file_path)
    dataframes[filename] = df
    print(f"Successfully loaded {filename}. First 5 rows:")
    print(df.head())
    print("\n---\n")
print("All specified files processed.")
print("You can access the DataFrames using the 'dataframes' dictionary, e.g., `dataframes['s2_response_nr.csv']`")
print('test commit')