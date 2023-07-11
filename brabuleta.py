import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parâmetros do atrator de Lorenz
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0

# Função de derivação do sistema de Lorenz
def lorenz_deriv(xyz):
    x, y, z = xyz
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z
    return dx_dt, dy_dt, dz_dt

# Solução numérica do sistema de Lorenz


dt = 0.01
t = np.arange(0, 100, dt)
#xyz0 = (1.0, 1.0, 1.0)
xyz0 = (-8.0, 8.0, 27.0)  # Condições iniciais anotar possiveis locais
xyz = np.zeros((len(t), 3))
xyz[0] = xyz0
for i in range(len(t) - 1):
    dx_dt, dy_dt, dz_dt = lorenz_deriv(xyz[i])
    xyz[i + 1] = xyz[i] + dt * np.array([dx_dt, dy_dt, dz_dt])

# Configuração do gráfico 3D
fig = plt.figure(dpi=150)  #passando dpi como argumento eu mudo a resolução do gráfico
#plt.style.use('dark_background') #ainda testar fundo preto
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim((-30, 30)) #limita o gráfico no eixo x
ax.set_ylim((-30, 30)) #limita o gráfico no eixo y
ax.set_zlim((0, 60)) #limita o gráfico no eixo z
ax.set_xlabel('Eixo X', style='italic')
ax.set_ylabel('Eixo Y', style='italic')
ax.set_zlabel('Eixo Z', style='italic')
ax.set_title('Atrator de Lorenz', style='italic', color='black', fontsize=20, fontweight='bold')
# Definição do gráfico, titulo, estilo, etc

# Inicialização do gráfico
line, = ax.plot([], [], [], 'k-', lw=1.0)

# Função de inicialização


def init():
    line.set_data([], [])
    line.set_3d_properties([])
    return line,


# Função de atualização do frame
def update(frame):
    line.set_data(xyz[:frame, 0], xyz[:frame, 1])
    line.set_3d_properties(xyz[:frame, 2])
    return line,


# Criação da animação

ani = FuncAnimation(fig, update, frames=len(t), init_func=init, interval=10, blit=True)
#len(t) faz com que os frames fiquem a cada interação de tempo
# Mostra o gráfico animado
plt.show()
