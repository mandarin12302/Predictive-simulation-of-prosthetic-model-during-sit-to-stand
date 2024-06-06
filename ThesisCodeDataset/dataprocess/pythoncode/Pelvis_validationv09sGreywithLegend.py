import pandas as pd
import matplotlib.pyplot as plt
import glob
import numpy as np
from functools import reduce
import matplotlib.patches as mpatches
# File paths for your .sto files
file_paths = glob.glob('D:/thesis2/MATLAB_code/dataprocess/kinematic_kinatic/shreshold/KS*.sto')

# New data file
new_file_path = 'D:/thesis2/MATLAB_code/dataprocess/kinematic_kinatic/shreshold/P1242_C101.sto'
new_df = pd.read_csv(new_file_path, skiprows=6, sep='\s+')

# Truncate the new data frame at time 0.9s
new_df = new_df[new_df['time'] <= 0.9]

# Initialize lists to store all dataframes and times
dfs = []
times = []

# Loop through each file, load the data, and store the dataframes and times
for file_path in file_paths:
    df = pd.read_csv(file_path, skiprows=6, sep='\t')
    df = df[df['time'] <= 0.9]
    dfs.append(df)
    times.append(df['time'])

# Find the common time range across all dataframes
common_time = reduce(np.intersect1d, times)
# Initialize lists to store all 'pelvis_tx' and 'pelvis_ty' values
pelvis_tx_values = []
pelvis_ty_values = []

# Loop through each dataframe and store the 'pelvis_tx' and 'pelvis_ty' values pelvis.com_pos_x pelvis.com_pos_y
for df in dfs:
    df = df[df['time'].isin(common_time)]
    pelvis_tx_values.append(df['pelvis.com_pos_x'])
    pelvis_ty_values.append(df['pelvis.com_pos_y'])

# Convert the lists to numpy arrays
pelvis_tx_values = np.array(pelvis_tx_values)
pelvis_ty_values = np.array(pelvis_ty_values)

# Calculate the minimum and maximum 'pelvis_tx' and 'pelvis_ty' values
pelvis_tx_min = np.min(pelvis_tx_values, axis=0)
pelvis_tx_max = np.max(pelvis_tx_values, axis=0)
pelvis_ty_min = np.min(pelvis_ty_values, axis=0)
pelvis_ty_max = np.max(pelvis_ty_values, axis=0)


# Set the default font size
plt.rcParams.update({'font.size': 15})
# Plot setup for 'pelvis_tx'
plt.figure(figsize=(12, 6))

# Plot the grey band for 'pelvis_tx'
plt.fill_between(common_time, pelvis_tx_min, pelvis_tx_max, color='grey', alpha=0.5)

# Plot 'pelvis.pos.x' from the new data file
linex,=plt.plot(new_df['time'], new_df['pelvis.pos.x'], label='Experiment Data', linestyle='--', color='red')

# Create a Patch for the grey band
grey_patch = mpatches.Patch(color='grey', alpha=0.5, label='Simulation Results Data Range')

# Finalizing the plot for 'pelvis_tx'
plt.xlabel('Time (s)')
plt.ylabel('Pelvis x(m)')
plt.title('Pelvis COM Position in Horizontal Direction Over Time')
plt.legend(handles=[linex, grey_patch])
plt.show()

# Plot setup for 'pelvis_ty'
plt.figure(figsize=(12, 6))

# Plot the grey band for 'pelvis_ty'
plt.fill_between(common_time, pelvis_ty_min, pelvis_ty_max, color='grey', alpha=0.5)

# Plot 'pelvis.pos.y' from the new data file
liney,=plt.plot(new_df['time'], new_df['pelvis.pos.y'], label='Experiment Data', linestyle='--', color='red')

# Create a Patch for the grey band
grey_patch = mpatches.Patch(color='grey', alpha=0.5, label='Simulation Results Data Range')

# Finalizing the plot for 'pelvis_ty'
plt.xlabel('Time (s)')
plt.ylabel('Pelvis y(m)')
plt.title('Pelvis COM Position in Vertical Direction Over Time')
plt.legend(handles=[liney, grey_patch])
plt.show()