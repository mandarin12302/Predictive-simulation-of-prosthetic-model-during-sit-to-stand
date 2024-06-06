import matplotlib.pyplot as plt

# Data from the table
file_names = ['KS00', 'KS10', 'KS20', 'KS30', 'KS40', 'KS50', 'KS60', 'KS70', 'KS80', 'KS90']
knee_stiffness = [1.26, 10.09, 20.34, 30.11, 39.88, 49.82, 59.8, 70.13, 80.09, 90.4]
cubed_muscle_stress = [175.104, 172.04, 116.046, 104.225, 108.041, 101.427, 103.168, 118.839, 129.186, 177.454]
effort = [243.335, 256.958, 196.98, 183.199, 189.421, 173.931, 180.617, 186.562, 189.259, 205.904]
total_effort = [418.439, 428.998, 313.026, 287.424, 297.462, 275.358, 283.785, 305.401, 318.445, 383.358]
plt.rcParams.update({'font.size': 15})
# Plotting the line chart
plt.figure(figsize=(12, 6))
plt.plot(knee_stiffness, cubed_muscle_stress, marker='o', linestyle='-', label='Cubed Muscle Stress')
plt.plot(knee_stiffness, effort, marker='o', linestyle='--', label='Effort')
plt.plot(knee_stiffness, total_effort, marker='o', linestyle='-.', label='Total Effort')

# Adding titles and labels
plt.title('Cubed Muscle Stress, Effort, and Total Effort vs. Knee Stiffness Settings')
plt.xlabel('Knee Stiffness (Nms/rad)')
plt.ylabel('Values')
plt.legend()
#plt.grid(True)

# Display the plot
plt.show()
