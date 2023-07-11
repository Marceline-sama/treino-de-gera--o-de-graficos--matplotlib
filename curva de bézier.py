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
    t_values = np.linspace(0, 1, 100)
    curve_points = np.array([bezier_curve(points, t) for t in t_values])
    #plt.plot(points[:, 0], points[:, 1], '--o')#imprime os pontos de controle
    plt.plot(curve_points[:, 0], curve_points[:, 1], label='Curva de Bézier')
    plt.scatter(points[:, 0], points[:, 1], c='blue', label='Pontos de Controle')
    plt.legend()#cria a legenda
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Curva de Bézier de Grau 3')#imprime o título
    plt.grid(True)#adiciona a grid
    plt.show()#método padrão de impressão do gráfico


# Pontos de controle
points = np.array([[1, 1], [2, 4], [4, 3], [5, 2]])


plot_bezier_curve(points)
