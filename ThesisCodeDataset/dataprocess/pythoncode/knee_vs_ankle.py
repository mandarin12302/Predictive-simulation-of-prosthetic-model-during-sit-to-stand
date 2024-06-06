import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

# File paths for your .sto files
file_paths = glob.glob('D:/thesis2/MATLAB_code/dataprocess/kinematic_kinatic/shreshold/KS*.sto')

# Loop through each file, load the data, and plot
for file_path in file_paths:
    # Load the data, skipping the first 6 rows, and use the 7th row as headers
    df = pd.read_csv(file_path, skiprows=6, sep='\t')
    plt.rcParams.update({'font.size': 15})
    # Plot setup
    plt.figure(figsize=(12, 6))
    
    # Plot 'knee_angle_l' vs 'ankle_angle_l' with solid line
    plt.plot(df['knee_angle_l'], df['ankle_angle_l'], label='Intact Side', linestyle='-')
    
    # Plot 'knee_angle_r' vs 'ankle_angle_r' with dashed line
    plt.plot(df['knee_angle_r'], df['ankle_angle_r'], label='Prosthetic Side', linestyle='--')

    # Extract file name from file path
    file_name = os.path.basename(file_path).split('.')[0]

    # Finalizing the plot
    plt.xlabel('Knee Angle (radians)')
    plt.ylabel('Ankle Angle (radians)')
    plt.title(f'Ankle Angle vs Knee Angle of {file_name}')
    plt.legend()
    plt.show()