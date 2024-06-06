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
    # Find the time when 'com_y' first equals or is bigger than 0.9
    time_com_y = df[df['com_y'] >= 0.9]['time'].iloc[0] if any(df['com_y'] >= 0.9) else None
    # Calculate average loads for each joint during the time from 0 to time_com_y
    avg_loads_before = df[df['time'] <= time_com_y].mean() if time_com_y is not None else df.mean()
    # Calculate average loads for each joint during the time from time_com_y to the end
    avg_loads_after = df[df['time'] > time_com_y].mean() if time_com_y is not None else df.mean()
    # Calculate peak loads for each joint during the time from 0 to time_com_y
    peak_loads_before = df[df['time'] <= time_com_y].max() if time_com_y is not None else df.max()
    # Calculate peak loads for each joint during the time from time_com_y to the end
    peak_loads_after = df[df['time'] > time_com_y].max() if time_com_y is not None else df.max()
    return avg_loads_before, avg_loads_after, peak_loads_before, peak_loads_after, time_com_y

# Define the pairs of joints for the line charts
joint_pairs = [('knee_l.load', 'knee_r.load'), ('hip_l.load', 'hip_r.load'), 
               ('ankle_l.load', 'ankle_r.load'), ('leg0_l.grf_norm_y', 'leg1_r.grf_norm_y'),('lumbar_joint.load', 'thorax_joint.load')]

# List of file paths
file_paths = glob.glob('D:/thesis2/MATLAB_code/dataprocess/kinematic_kinatic/shreshold/KS*.sto')
# Define the mapping from original joint names to new names
joint_name_mapping = {
    'knee_l.load': 'Intact side knee load',
    'knee_r.load': 'Prosthetic side knee load',
    'hip_l.load': 'Intact side hip load',
    'hip_r.load': 'Prosthetic side hip load',
    'ankle_l.load': 'Intact side ankle load',
    'ankle_r.load': 'Prosthetic side ankle load',
    'leg0_l.grf_norm_y': 'Intact side side normalized GRF',
    'leg1_r.grf_norm_y': 'Prosthetic side side normalized GRF',
    'lumbar_joint.load': 'Lumbar joint load',
    'thorax_joint.load': 'Thorax joint load'
}
# Variables for plotting
file_names = [os.path.splitext(os.path.basename(fp))[0] for fp in file_paths]
avg_values_before_all_files = [load_and_get_peaks(fp)[0] for fp in file_paths]
avg_values_after_all_files = [load_and_get_peaks(fp)[1] for fp in file_paths]
peak_values_before_all_files = [load_and_get_peaks(fp)[2] for fp in file_paths]
peak_values_after_all_files = [load_and_get_peaks(fp)[3] for fp in file_paths]
time_com_y_all_files = [load_and_get_peaks(fp)[4] for fp in file_paths]


plt.rcParams.update({'font.size': 15})


for joint1, joint2 in joint_pairs:
    # Get the average and peak loads for these joints across all files
    joint1_values_before = [avg_values_before_all_files[file_names.index(fn)][joint1] for fn in file_names]
    joint1_values_after = [avg_values_after_all_files[file_names.index(fn)][joint1] for fn in file_names]
    joint1_peak_values_before = [peak_values_before_all_files[file_names.index(fn)][joint1] for fn in file_names]
    joint1_peak_values_after = [peak_values_after_all_files[file_names.index(fn)][joint1] for fn in file_names]

    joint2_values_before = [avg_values_before_all_files[file_names.index(fn)][joint2] for fn in file_names]
    joint2_values_after = [avg_values_after_all_files[file_names.index(fn)][joint2] for fn in file_names]
    joint2_peak_values_before = [peak_values_before_all_files[file_names.index(fn)][joint2] for fn in file_names]
    joint2_peak_values_after = [peak_values_after_all_files[file_names.index(fn)][joint2] for fn in file_names]

    # Prepare the figure
    # Find minimum and maximum values for these joints
    joint_min = 0#min(min(joint1_values_before), min(joint1_values_after), min(joint2_values_before), min(joint2_values_after))
    joint_max = max(max(joint1_values_before), max(joint1_values_after), max(joint2_values_before), max(joint2_values_after))

    joint_min = 0#min(
    #min(joint1_values_before), min(joint1_values_after),
    #min(joint2_values_before), min(joint2_values_after),
    #min(joint1_peak_values_before), min(joint1_peak_values_after),
    #min(joint2_peak_values_before), min(joint2_peak_values_after)
#)
    joint_max = max(
    max(joint1_values_before), max(joint1_values_after),
    max(joint2_values_before), max(joint2_values_after),
    max(joint1_peak_values_before), max(joint1_peak_values_after),
    max(joint2_peak_values_before), max(joint2_peak_values_after)
)

    # Prepare the figure
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))#9figsize=(10, 12)

    # Plot the data
    ax1.plot(file_names, joint1_values_before, marker='o', linestyle='-', label='Average Before com_y >= 0.9')
    ax1.plot(file_names, joint1_values_after, marker='o', linestyle='--', label='Average After com_y >= 0.9')
    ax1.plot(file_names, joint1_peak_values_before, marker='o', linestyle='-.', label='Peak Before com_y >= 0.9')
    ax1.set_title(joint_name_mapping.get(joint1, joint1))
    ax1.set_xlabel('Knee stiffness (Nm/rad)')
    ax1.set_ylabel('Average Load (Body Weight)')
    ax1.set_ylim(joint_min, joint_max)  # Set y-axis limits
    ax1.legend()

    ax2.plot(file_names, joint2_values_before, marker='o', linestyle='-', label='Average Before com_y >= 0.9')
    ax2.plot(file_names, joint2_values_after, marker='o', linestyle='--', label='Average After com_y >= 0.9')
    ax2.plot(file_names, joint2_peak_values_before, marker='o', linestyle='-.', label='Peak Before com_y >= 0.9')
    ax2.set_title(joint_name_mapping.get(joint2, joint2))
    ax2.set_xlabel('Knee stiffness (Nm/rad)') 
    ax2.set_ylabel('Average Load (Body Weight)') 
    ax2.set_ylim(joint_min, joint_max)  # Set y-axis limits
    ax2.legend()

    # Display the plot
    plt.tight_layout()
    plt.show()