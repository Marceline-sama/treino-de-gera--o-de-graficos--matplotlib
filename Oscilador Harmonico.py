import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Função de define o Método Runge-Kutta de 4a ordem
def rk4(f, h, t0, C0, t_max):
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
    k = 1  # constante elástica da mola
    m = 1  # massa
    return np.array([v[1], -(k / m) * v[0]])

# chama a rotina rk4 para obter as soluções da EDO
h = 0.1  # passo de integração
t0 = 0  # tempo inicial
C0 = [1, 0]  # Condições inciais
t_max = 20  # tempo máximo
t, x = rk4(f, h, t0, C0, t_max)

#TESTE ANIMAÇÂO 1.0

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)#lw é o tamanho da linha

#inicia a animação
def init():
    ax.set_xlim(0, t_max)
    ax.set_ylim(-1.5, 1.5)#limite da oscilação
    return line,

#função que atualiza os quadros
def update(frame):
    line.set_data(t[:frame], x[:frame, 0])#passar os parametros que atualizam os dados da linha com um deslocamento
    return line,

#cria a animação
ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True)

#plota o gráfico simples
plt.title('Oscilador Harmonico')
plt.grid(True)
plt.ylabel('Eixo Y')
plt.xlabel('Eixo X')

plt.show()