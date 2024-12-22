import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression

# Título principal
st.title("NanoTecAnnaDalmoneki")
st.subheader("Simulação de IA para Nanotecnologia")
st.markdown("### Explore interações de partículas e inteligência artificial!")

# Configurações no painel lateral
st.sidebar.header("Configurações")
num_particles = st.sidebar.slider("Número de Partículas", 10, 100, 50)
steps = st.sidebar.slider("Número de Passos", 10, 500, 100)

# Inicializar partículas
x = np.random.uniform(0, 10, num_particles)
y = np.random.uniform(0, 10, num_particles)
vx = np.random.uniform(-0.5, 0.5, num_particles)
vy = np.random.uniform(-0.5, 0.5, num_particles)

# Simulação de Movimento com Frames Estáticos
st.markdown("### Simulação de Movimento")
if st.sidebar.button("Iniciar Simulação"):
    st.markdown("**Movimento das Partículas**")
    for step in range(1, 6):  # Mostra apenas 5 frames para simplicidade
        # Atualizar posições
        x += vx
        y += vy
        x = np.clip(x, 0, 10)
        y = np.clip(y, 0, 10)

        # Criar gráfico estático
        fig, ax = plt.subplots()
        ax.scatter(x, y, s=50, alpha=0.7, label="Partículas")
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_title(f"Frame {step}")
        ax.legend()
        st.pyplot(fig)

# Simulação com Clusters
st.markdown("### Agrupamento de Clusters")
if st.sidebar.button("Agrupar Partículas"):
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
