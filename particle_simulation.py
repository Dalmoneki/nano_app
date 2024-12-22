import matplotlib.pyplot as plt
import numpy as np

# Número de partículas e passos
num_particles = 100
steps = 200

# Inicializando posições das partículas
x = np.zeros(num_particles)
y = np.zeros(num_particles)

# Simulando o movimento
for step in range(steps):
    x += np.random.uniform(-1, 1, num_particles)
    y += np.random.uniform(-1, 1, num_particles)
    
    # Plotando as posições
    plt.clf()  # Limpa o gráfico
    plt.scatter(x, y, c='blue', alpha=0.6, s=10)
    plt.xlim(-100, 100)
    plt.ylim(-100, 100)
    plt.title(f"Passo {step + 1}")
    plt.pause(0.1)

plt.show()

