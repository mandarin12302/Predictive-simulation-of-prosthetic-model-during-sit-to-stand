import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
import os
from sklearn.linear_model import LinearRegression

def calculate_settling_time(times, values, percentage=0.1):
    model = LinearRegression()
    model.fit(np.array(times[-50:]).reshape(-1, 1), values[-50:])
    final_value = model.predict(np.array(times).reshape(-1, 1))
    threshold = percentage * final_value
    within_threshold = np.abs(values - final_value) < threshold
    for i in range(len(within_threshold)):
        if np.all(within_threshold[i:]):
            return times.iloc[i]
    return None

def load_and_analyze(file_path):
    df = pd.read_csv(file_path, delim_whitespace=True, skiprows=6)
    filename = os.path.basename(file_path)
    if 'com_y' in df.columns and any(df['com_y'] >= 0.9):
        stabilization_start_index = df[df['com_y'] >= 0.9].index[0]
        stabilization_start_time = df['time'][stabilization_start_index]
    else:
        stabilization_start_index = None
        stabilization_start_time = None

    if stabilization_start_index is not None:
        grf_left = df.loc[stabilization_start_index:, 'leg0_l.grf_norm_y']
        grf_right = df.loc[stabilization_start_index:, 'leg1_r.grf_norm_y']
        times = df['time'][stabilization_start_index:]
        window_size = 50
        grf_left_smooth = grf_left.rolling(window=window_size, min_periods=1).mean()
        grf_right_smooth = grf_right.rolling(window=window_size, min_periods=1).mean()
    else:
        return {"error": "No stabilization start found"}

    settling_time_left = calculate_settling_time(times, grf_left_smooth)
    settling_time_right = calculate_settling_time(times, grf_right_smooth)

    # Calculate the duration of the stabilization phase
    if settling_time_left is not None and settling_time_right is not None:
        stabilization_duration_left = settling_time_left - stabilization_start_time
        stabilization_duration_right = settling_time_right - stabilization_start_time
    else:
        stabilization_duration_left = None
        stabilization_duration_right = None
    fig, axs = plt.subplots(3, 1, figsize=(12, 18), sharex=True)

    axs[0].plot(df['time'], df['com_y'], label='Center of Mass Y')
    if stabilization_start_time is not None:
        axs[0].axvline(x=stabilization_start_time, color='g', linestyle='--', label='Stabilization Start')

    axs[0].set_title('Center of Mass Y  '+ filename)
    axs[0].set_xlabel('Time')
    axs[0].set_ylabel('com_y')
    axs[0].legend()

    axs[1].plot(df['time'], df['leg0_l.grf_norm_y'], label='Left Leg GRF')
    axs[1].plot(times, grf_left_smooth, label='Smoothed Left Leg GRF', linestyle='--')
    if stabilization_start_time is not None:
        axs[1].axvline(x=stabilization_start_time, color='g', linestyle='--', label='Stabilization Start')
    if settling_time_left is not None:
        axs[1].axvline(x=settling_time_left, color='r', linestyle='--', label='Settling Time')
    axs[1].set_title('Left Leg Ground Reaction Force')
    axs[1].set_xlabel('Time')
    axs[1].set_ylabel('GRF Normalized')
    axs[1].legend()

    axs[2].plot(df['time'], df['leg1_r.grf_norm_y'], label='Right Leg GRF')
    axs[2].plot(times, grf_right_smooth, label='Smoothed Right Leg GRF', linestyle='--')
    if stabilization_start_time is not None:
        axs[2].axvline(x=stabilization_start_time, color='g', linestyle='--', label='Stabilization Start')
    if settling_time_right is not None:
        axs[2].axvline(x=settling_time_right, color='r', linestyle='--', label='Settling Time')
    axs[2].set_title('Right Leg Ground Reaction Force')
    axs[2].set_xlabel('Time')
    axs[2].set_ylabel('GRF Normalized')
    axs[2].legend()

    plt.tight_layout()
    plt.show()

    return {
        'Stabilization Start Time': stabilization_start_time,
        'Left Leg Settling Time': settling_time_left,
        'Right Leg Settling Time': settling_time_right,
        'Left Leg Stabilization Duration': stabilization_duration_left,
        'Right Leg Stabilization Duration': stabilization_duration_right,
    }

file_paths = glob.glob('D:/thesis2/MATLAB_code/dataprocess/kinematic_kinatic/shreshold/KS*.sto')
results = []
for file_path in file_paths:
    result = load_and_analyze(file_path)
    results.append(result)

x_values = np.arange(0, 91, 10)  # Create a list of x-values from 0 to 90 with an increment of 10

plt.figure()
plt.plot(x_values, [result['Left Leg Stabilization Duration'] for result in results], label='Intact Side')
plt.plot(x_values, [result['Right Leg Stabilization Duration'] for result in results], label='Prosthetic Side')
plt.title('Stabilization Duration according to GRFs across all knee stiffness settings')
plt.xlabel('knee stiffness settings (Nm/rad)')
plt.ylabel('Stabilization Duration (s)')
plt.xticks(x_values)  # Set x-axis ticks to match your x-values
plt.legend()
plt.show()