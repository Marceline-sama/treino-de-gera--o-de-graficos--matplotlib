import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation


# Função que define o Método Runge-Kutta de 4ª ordem
def rk_4(f, h, t0, C0, t_max):
    # Número de iterações
    n = round((t_max - t0) / h) + 1

    # Dimensão da EDO
    dim = len(C0)

    # Tempo
    t = []
    t.append(t0)

    # Vetor solução da EDO para cada t
    Y = np.zeros((n, dim))

    # Atribui as condições iniciais
    Y[0, :] = C0

    # Calcula cada iteração
    for j in range(1, n):
        # Primeira inclinação
        k_1 = h * f(t[j - 1], Y[j - 1, :])

        # Segunda inclinação
        k_2 = h * f(t[j - 1] + h / 2, Y[j - 1, :] + (1 / 2) * k_1)

        # Terceira inclinação
        k_3 = h * f(t[j - 1] + h / 2, Y[j - 1, :] + (1 / 2) * k_2)

        # Quarta inclinação
        k_4 = h * f(t[j - 1] + h / 2, Y[j - 1, :] + k_3)

        # Obtém o Y atual usando a inclinação média ponderada
        Y[j, :] = Y[j - 1, :] + (1 / 6) * (k_1 + 2 * k_2 + 2 * k_3 + k_4)

        # Incrementa o tempo
        t.append(t[j - 1] + h)

    return t, Y


# Campo de vetores do efeito borboleta simples
def f(t, v):
    sigma = 10
    rho = 28
    beta = 8 / 3

    x = v[0]
    y = v[1]
    z = v[2]

    return np.array([sigma * (y - x), x * (rho - z) - y, x * y - beta * z])


# Chama a rotina rk4 para obter as soluções da EDO
h = 0.01  # Passo de integração
t0 = 0  # Tempo inicial
C0 = [-1, -1, 1]  # Condições iniciais
t_max = 20  # Tempo máximo
t, V = rk_4(f, h, t0, C0, t_max)

# Configuração inicial do gráfico
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-25, 25)
ax.set_ylim(-20, 20)
ax.set_zlim(0, 40)
ax.set_xlabel('Eixo x')
ax.set_ylabel('Eixo y')
ax.set_zlabel('Eixo z')
ax.set_title('Gráfico Butterfly Effect')


# Função de atualização do frame
def update(frame):
    ax.clear()
    ax.set_xlim(-25, 25)
    ax.set_ylim(-20, 20)
    ax.set_zlim(0, 40)
    ax.set_xlabel('Eixo x')
    ax.set_ylabel('Eixo y')
    ax.set_zlabel('Eixo z')
    ax.set_title('Gráfico Butterfly Effect')
    ax.plot(V[:frame, 0], V[:frame, 1], V[:frame, 2], color='green')
    return ax


# Cria a animação
ani = FuncAnimation(fig, update, frames=len(V), interval=100, blit=True)

# Mostra o gráfico animado
plt.show()
