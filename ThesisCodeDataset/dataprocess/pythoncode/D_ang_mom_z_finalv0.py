import pandas as pd
import matplotlib.pyplot as plt
import glob
import numpy as np
import os

# File paths for your .sto files
file_paths = glob.glob('D:/thesis2/MATLAB_code/dataprocess/kinematic_kinatic/shreshold/KS*.sto')

# Variables for storing max and min values of the derivative
max_derivatives = []
min_derivatives = []

# Loop through each file, load the data, and calculate the derivative
for file_path in file_paths:
    # Load the data, skipping the first 6 rows, and use the 7th row as headers
    df = pd.read_csv(file_path, skiprows=6, sep='\t')
    
    # Calculate the derivative of 'ang_mom_z' over 'time'
    df['ang_mom_z_derivative'] = df['ang_mom_z'].diff() / df['time'].diff()
    
    # Find the maximum and minimum of the derivative
    max_derivative = df['ang_mom_z_derivative'].max()
    min_derivative = df['ang_mom_z_derivative'].min()
    
    # Store the max and min values
    max_derivatives.append(max_derivative)
    min_derivatives.append(min_derivative)

# Prepare the figure for the max and min of the derivative
fig, ax = plt.subplots(figsize=(12, 6))

# Get the base names of the file paths without extensions
file_names = [os.path.splitext(os.path.basename(fp))[0] for fp in file_paths]

# Set the default font size
plt.rcParams.update({'font.size': 15})
# Plot the data
ax.plot(file_names, max_derivatives, marker='o', label='Max derivative')
ax.plot(file_names, min_derivatives, marker='o', label='Min derivative')

# Annotate each point with its value
for i, (max_derivative, min_derivative) in enumerate(zip(max_derivatives, min_derivatives)):
    ax.annotate(f'{max_derivative:.2f}', (file_names[i], max_derivative), textcoords="offset points", xytext=(-15,-15), ha='center')
    ax.annotate(f'{min_derivative:.2f}', (file_names[i], min_derivative), textcoords="offset points", xytext=(-15,-15), ha='center')

ax.set_title('Max and Min of the Derivative of Whole Body Angular Momentum over time across all knee stiffness settings')
ax.set_xlabel('knee stiffness settings (Nm/rad)')
ax.set_ylabel('Change of Angular momentum (kg·m^2/s^2)')

# Display the plot
plt.legend()
plt.tight_layout()
plt.show()