import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Função de define o Método Runge-Kutta de 4a ordem
def rk_4(f, h, t0, C0, t_max):
    # número de iterações
    n = round((t_max - t0) / h) + 1

    # dimensão da EDO
    dim = len(C0)

    # tempo
    t = []
    t.append(t0)

    # vetor solução da EDO para cada t
    Y = np.zeros((n, dim))

    # atribiu as condições iniciais
    Y[0, :] = C0

    # calcula cada iteração
    for j in range(1, n):
        # primeira inclinação
        k_1 = h * f(t[j - 1], Y[j - 1, :])

        # segunda inclinação
        k_2 = h * f(t[j - 1] + h / 2, Y[j - 1, :] + (1 / 2) * k_1)

        # terceira inclinação
        k_3 = h * f(t[j - 1] + h / 2, Y[j - 1, :] + (1 / 2) * k_2)

        # quarta inclinação
        k_4 = h * f(t[j - 1] + h / 2, Y[j - 1, :] + k_3)

        # obtém o Y atual usando a inclinação média ponderada
        Y[j, :] = Y[j - 1, :] + (1 / 6) * (k_1 + 2 * k_2 + 2 * k_3 + k_4)

        # incrementa o tempo
        t.append(t[j - 1] + h)

    return t, Y


# campo de vetores do oscilador harmônico simples
def f(t, v):
    sigma = 10
    rho = 28
    beta = 8 / 3

    x = v[0]
    y = v[1]
    z = v[2]

    return np.array([sigma * (y - x), x * (rho - z) - y, x * y - beta * z])

# chama a rotina rk4 para obter as soluções da EDO
h = 0.01  # passo de integração
t0 = 0  # tempo inicial
C0 = [-1, -1, 1]  # Condições inciais
t_max = 20  # tempo máximo
t, V = rk_4(f, h, t0, C0, t_max)

# Plot
fig = 
ax = plt.figure().add_subplot(projection='3d')

ax.plot(*V.T, lw=1)

plt.show()






