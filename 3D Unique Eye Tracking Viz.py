import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Dataset (same as before)
fixation_point_x = [
    48.537, 49.675, 40.357, 27.152, 35.165, 57.335, 66.603, 80.961, 80.878, 88.915,
    74.779, 72.428, 46.923, 17.203, 16.492, 15.128, 14.277, 19.473, 32.567, 25.118,
    17.517, 39.376, 52.920, 75.061, 74.053, 76.329, 55.320, 57.869
]
fixation_point_y = [
    70.049, 81.500, 55.686, 25.651, 22.706, 36.569, 28.471, 32.100, 27.835, 35.176,
    51.111, 70.449, 79.673, 88.145, 84.230, 31.822, 29.020, 30.560, 38.121, 41.769,
    39.815, 41.369, 36.210, 47.794, 46.111, 36.528, 38.370, 38.623
]
fixation_duration_ms = [
    125, 310, 375, 341, 310, 372, 152, 369, 385, 308, 372, 371, 92, 376, 217, 370,
    123, 215, 371, 371, 248, 400, 396, 373, 186, 374, 371
]

# Normalize the durations to create a depth map
durations = np.array(fixation_duration_ms)
durations = (durations - np.nanmin(durations)) / (np.nanmax(durations) - np.nanmin(durations)) * 10  # Scaled to 10 for depth

# Ensure all arrays have the same length by truncating to the minimum length
min_length = min(len(fixation_point_x), len(fixation_point_y), len(fixation_duration_ms))

fixation_point_x = fixation_point_x[:min_length]
fixation_point_y = fixation_point_y[:min_length]
durations = durations[:min_length]

# Create 3D visualization
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# 3. Spiral and curved paths
theta = np.linspace(0, 2*np.pi, len(fixation_point_x))
x = fixation_point_x + np.sin(theta)*5
y = fixation_point_y + np.cos(theta)*5

for i in range(len(x)-1):
    ax.plot([x[i], x[i+1]], [y[i], y[i+1]], [durations[i], durations[i+1]], color='black', linewidth=2, alpha=0.5)

# Set the axis labels
ax.set_xlabel('X Coordinates')
ax.set_ylabel('Y Coordinates')
ax.set_zlabel('Duration (Depth)')

# Hide the grid for a cleaner aesthetic
ax.grid(False)

# Set a custom view angle
ax.view_init(elev=45, azim=90)

plt.title('Spiral 3D Fixation Map (Black)')
plt.show()


