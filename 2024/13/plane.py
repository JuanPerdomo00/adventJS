import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sys

# Coordenadas que el robot seguirá
coordinates = [(0, 1), (1, 2), (-2, 3), (0, 0)]

# Configuración de la figura y los ejes
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.axhline(0, color="black", linewidth=0.8)
ax.axvline(0, color="black", linewidth=0.8)

# Inicializar el "robot" en la primera posición
(robot,) = ax.plot([], [], "o", color="red", markersize=12, label="🤖")


# Función para actualizar la posición del robot
def update(frame):
    x, y = coordinates[frame]
    robot.set_data([x], [y])  # Asegúrate de pasar listas
    return (robot,)


# Crear la animación
ani = FuncAnimation(fig, update, frames=len(coordinates), interval=1000, repeat=False)

# Guardar la animación como video
ani.save(f"{sys.argv[1]}.mp4", writer="ffmpeg", dpi=300)
