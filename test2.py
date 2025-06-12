import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def create_ring(radius, thickness):
    # Create the ring vertices.
    vertices = np.array([
        [radius, 0, 0],
        [radius, thickness, 0],
        [-radius, thickness, 0],
        [-radius, 0, 0],
        [radius, 0, 0]
    ])

    # Create the ring faces.
    faces = np.array([
        [0, 1, 2],
        [2, 3, 0]
    ])

    # Return the vertices and faces.
    return vertices, faces
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
vertices, faces = create_ring(1, 0.1)
ax.plot_trisurf(vertices[:, 0], vertices[:, 1], vertices[:, 2], triangles=faces, color='blue')
def update_ring(frame):
    # Rotate the ring around the y-axis.
    vertices[:, 1] = np.sin(frame / 10)

    # Update the plot.
    ax.clear()
    ax.plot_trisurf(vertices[:, 0], vertices[:, 1], vertices[:, 2], triangles=faces, color='blue')

ani = animation.FuncAnimation(fig, update_ring, interval=100)
plt.show()