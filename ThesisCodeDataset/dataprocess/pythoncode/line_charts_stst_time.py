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
    # Find the time when 'com_y' first equals or is bigger than 0.9
    time_com_y = df[df['com_y'] >= 0.9]['time'].iloc[0] if any(df['com_y'] >= 0.9) else None
    return peak_loads, min_loads, time_com_y

# Define the order of the joints for the line charts
joint_order = ['com_y']

# List of file paths
file_paths = glob.glob('D:/thesis2/MATLAB_code/dataprocess/kinematic_kinatic/shreshold/KS*.sto')

# Variables for plotting
file_names = [os.path.splitext(os.path.basename(fp))[0] for fp in file_paths]
peak_values_all_files = [load_and_get_peaks(fp)[0][joint_order] for fp in file_paths]
min_values_all_files = [load_and_get_peaks(fp)[1][joint_order] for fp in file_paths]
time_com_y_all_files = [load_and_get_peaks(fp)[2] for fp in file_paths]

# Prepare the figure for time_com_y_all_files
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the data
ax.plot(file_names, time_com_y_all_files, marker='o', label='Time when com_y >= 0.9')

# Annotate each point with its time value
for i, time in enumerate(time_com_y_all_files):
    ax.annotate(str(time), (file_names[i], time))

ax.set_title('Time when com_y >= 0.9')
ax.set_xlabel('File')
ax.set_ylabel('Time')

# Display the plot
plt.legend()
plt.tight_layout()
plt.show()