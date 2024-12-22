import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Configurações iniciais
num_particles = 50
steps = 100
x = np.random.uniform(0, 10, num_particles)
y = np.random.uniform(0, 10, num_particles)
vx = np.random.uniform(-0.5, 0.5, num_particles)
vy = np.random.uniform(-0.5, 0.5, num_particles)

# Função para atualizar as posições
def update_positions(i):
    global x, y, vx, vy
    x += vx
    y += vy

    # Limites para manter partículas no gráfico
    x = np.clip(x, 0, 10)
    y = np.clip(y, 0, 10)

    scat.set_offsets(np.c_[x, y])

# Criando o gráfico
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
scat = ax.scatter(x, y, s=50, alpha=0.7)

# Animação
ani = FuncAnimation(fig, update_positions, frames=steps, interval=100)
plt.show()
