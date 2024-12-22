import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression

# Configuração do Título
st.title("NanoTecAnnaDalmoneki - Simulação de IA para Nanotecnologia")
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
    st.subheader("Predição com Machine Learning")
    # Simular posições finais para gerar dados
    simulated_steps = np.random.randint(50, 500, size=100).reshape(-1, 1)
    simulated_positions = simulated_steps * 0.5 + np.random.uniform(0, 2, size=(100, 1))
    
    # Treinar o modelo
    model = LinearRegression()
    model.fit(simulated_steps, simulated_positions)

    # Prever com base no número de passos configurado
    predicted_position = model.predict([[steps]])[0][0]
    st.write(f"**Posição média final prevista:** {predicted_position:.2f}")

# Simulação com Gráfico Interativo
st.subheader("Gráfico Interativo")
if st.sidebar.button("Exibir Gráfico de Movimento"):
    fig, ax = plt.subplots()
    ax.scatter(x, y, s=50, alpha=0.7, label="Partículas")
    ax.set_title("Movimento das Partículas")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.legend()
    st.pyplot(fig)

# Simulação com Clusters
if st.sidebar.button("Agrupar em Clusters"):
    st.subheader("Agrupamento de Clusters")
    # Atualizar posições finais
    x += vx * steps
    y += vy * steps
    x = np.clip(x, 0, 10)
    y = np.clip(y, 0, 10)

    # Agrupar com K-Means
    positions = np.column_stack((x, y))
    kmeans = KMeans(n_clusters=3, random_state=0).fit(positions)
    labels = kmeans.labels_

    # Visualizar clusters
    fig, ax = plt.subplots()
    for cluster in range(3):
        cluster_points = positions[labels == cluster]
        ax.scatter(cluster_points[:, 0], cluster_points[:, 1], label=f"Cluster {cluster+1}", alpha=0.7)
    ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], color='red', label="Centros", marker="X")
    ax.set_title("Agrupamento de Clusters")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.legend()
    st.pyplot(fig)
