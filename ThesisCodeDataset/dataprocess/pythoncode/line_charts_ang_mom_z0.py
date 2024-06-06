# line_charts.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import pi
import glob
import os

# Define the load_and_get_peaks function here
def load_and_get_peaks(file_path):
    # Load the data
    df = pd.read_csv(file_path, delim_whitespace=True, skiprows=6)
    # Calculate peak and minimum loads for each joint
    peak_loads = df.max()
    min_loads = df.min()
    return peak_loads, min_loads

# Define the order of the joints for the line charts
joint_order = ['ang_mom_z']

# List of file paths
file_paths = glob.glob('D:/thesis2/MATLAB_code/dataprocess/kinematic_kinatic/shreshold/KS*.sto')

# Variables for plotting
file_names = [os.path.splitext(os.path.basename(fp))[0] for fp in file_paths]
peak_values_all_files = [load_and_get_peaks(fp)[0][joint_order] for fp in file_paths]
min_values_all_files = [load_and_get_peaks(fp)[1][joint_order] for fp in file_paths]
# Set the default font size
plt.rcParams.update({'font.size': 15})
for i, joint in enumerate(joint_order):
    # Get the peak and minimum loads for this joint across all files
    joint_peak_values = [peak_values_all_files[file_names.index(fn)][i] for fn in file_names]
    joint_min_values = [min_values_all_files[file_names.index(fn)][i] for fn in file_names]

    # Prepare the figure
    fig, ax = plt.subplots(figsize=(12, 6))

    # Plot the data
    ax.plot(file_names, joint_peak_values, marker='o', label='Peak Load')
    ax.plot(file_names, joint_min_values, marker='o', label='Min Load')
    ax.set_title('Max and Min Whole Body Angular Momentum about COM across all knee stiffness settings')
    ax.set_xlabel('Knee stiffness settings (Nm/rad)')
    ax.set_ylabel('Angular momentum (kg·m^2/s)')

    # Display the plot
    plt.legend()
    plt.tight_layout()
    plt.show()