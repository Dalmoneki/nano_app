import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Parâmetros da simulação
num_particles = 50
steps = 100

# Inicializando posições das partículas
x = np.zeros(num_particles)
y = np.zeros(num_particles)

# Dados para IA
historical_data = []

# Simulação e Treinamento
for step in range(steps):
    # Atualizar posições com movimento aleatório
    dx = np.random.uniform(-1, 1, num_particles)
    dy = np.random.uniform(-1, 1, num_particles)
    x += dx
    y += dy

    # Registrar histórico para IA
    for i in range(num_particles):
        historical_data.append([x[i], y[i]])

    # Treinar IA a cada 20 passos
    if step > 0 and step % 20 == 0:
        historical_data = np.array(historical_data)
        X_train = historical_data[:-num_particles]
        y_train = historical_data[num_particles:]

        model = LinearRegression()
        model.fit(X_train, y_train)

        # Previsão para o próximo movimento
        predicted = model.predict(historical_data[-num_particles:])
        x_predicted = predicted[:, 0]
        y_predicted = predicted[:, 1]

        # Plotar resultados
        plt.clf()
        plt.scatter(x, y, c='blue', label='Real', alpha=0.5)
        plt.scatter(x_predicted, y_predicted, c='red', label='Previsto', alpha=0.5)
        plt.legend()
        plt.title(f"Passo {step}")
        plt.pause(0.5)

plt.show()
