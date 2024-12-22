import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression

# Configuração do Título
st.title("Simulação de IA para Nanotecnologia - Dalmoneki; Anna")
st.markdown("Explore movimentos de partículas, predições e agrupamentos usando inteligência artificial!")

# Configurações Iniciais
st.sidebar.header("Configurações")
num_particles = st.sidebar.slider("Número de Partículas", 10, 100, 50)
steps = st.sidebar.slider("Número de Passos", 10, 500, 100)

# Inicializar partículas
x = np.random.uniform(0, 10, num_particles)
y = np.random.uniform(0, 10, num_particles)
vx = np.random.uniform(-0.5, 0.5, num_particles)
vy = np.random.uniform(-0.5, 0.5, num_particles)

# Predição com Machine Learning
if st.sidebar.button("Prever Posição Média Final"):
    # Simular posições finais para gerar dados
    simulated_steps = np.random.randint(50, 500, size=100).reshape(-1, 1)
    simulated_positions = simulated_steps * 0.5 + np.random.uniform(0, 2, size=(100, 1))
    
    # Treinar o modelo
    model = LinearRegression()
    model.fit(simulated_steps, simulated_positions)

    # Prever com base no número de passos configurado
    predicted_position = model.predict([[steps]])[0][0]
    st.write(f"**Posição média final prevista:** {predicted_position:.2f}")

# Simulação com Clusters
if st.sidebar.button("Agrupar em Clusters"):
    # Atualizar posições finais
    x += vx * steps
    y += vy * steps
    x = np.clip(x, 0, 10)
    y = np.clip(y, 0, 10)

    # Agrupar com K-Means
    positions = np.column_stack((x, y))
