import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def bezier_curve(points, t):
    n = len(points) - 1
    result = np.zeros(2)
    for i in range(n + 1):
        result += comb(n, i) * ((1 - t) ** (n - i)) * (t ** i) * points[i]
    return result

def comb(n, k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))

def plot_bezier_curve(points):
    fig, ax = plt.subplots()
    t_values = np.linspace(0, 1, 100)
    curve_points = np.array([bezier_curve(points, t) for t in t_values])

    line, = ax.plot([], [], label='Curva de Bézier')
    scatter = ax.scatter(points[:, 0], points[:, 1], c='blue', label='Pontos de Controle')

    ax.legend()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Curva de Bézier de Grau 3')
    ax.grid(True)

    def init():
        line.set_data([], [])
        return line,

    def update(frame):
        line.set_data(curve_points[:frame, 0], curve_points[:frame, 1])
        scatter.set_offsets(points)
        scatter.set_label(f'Pontos de Controle ({frame+1})')
        ax.legend()
        return line,

    # Cria a animação
    animation = FuncAnimation(fig, update, frames=len(curve_points), init_func=init, blit=True)

    plt.show()

# Pontos de controle
points = np.array([[1, 1], [2, 4], [4, 3], [5, 2]])

plot_bezier_curve(points)
