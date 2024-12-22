import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Configuração inicial
num_particles = 50
steps = 100
x = np.zeros(num_particles)
y = np.zeros(num_particles)
historical_data = []

def update_positions(x, y, num_particles):
    dx = np.random.uniform(-1, 1, num_particles)
    dy = np.random.uniform(-1, 1, num_particles)
    return x + dx, y + dy

def add_to_historical(historical_data, x, y):
    for i in range(len(x)):
        historical_data.append([x[i], y[i]])
    return historical_data

def train_and_predict(historical_data, num_particles):
    historical_data_np = np.array(historical_data)
    X_train = historical_data_np[:-num_particles]
    y_train = historical_data_np[num_particles:]
    model = LinearRegression()
    model.fit(X_train, y_train)
    predicted = model.predict(historical_data_np[-num_particles:])
    return predicted[:, 0], predicted[:, 1]

def plot_particles(x, y, x_predicted=None, y_predicted=None, step=0):
    plt.clf()
    plt.scatter(x, y, c='blue', label='Real', alpha=0.5)
    if x_predicted is not None and y_predicted is not None:
        plt.scatter(x_predicted, y_predicted, c='red', label='Previsto', alpha=0.5)
    plt.legend()
    plt.title(f"Passo {step}")
    plt.pause(0.5)

for step in range(steps):
    x, y = update_positions(x, y, num_particles)
    historical_data = add_to_historical(historical_data, x, y)
    if step > 0 and step % 20 == 0:
        x_predicted, y_predicted = train_and_predict(historical_data, num_particles)
        plot_particles(x, y, x_predicted, y_predicted, step)
    else:
        plot_particles(x, y, step=step)

plt.show()
