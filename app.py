import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import io

# Configuração do Título
st.title("Simulação de IA para Nanotecnologia - Dalmoneki; Anna")
st.markdown("Explore movimentos de partículas e interações utilizando inteligência artificial!")

# Configurações Iniciais
st.sidebar.header("Configurações")
num_particles = st.sidebar.slider("Número de Partículas", 10, 100, 50)
steps = st.sidebar.slider("Número de Passos", 10, 500, 100)

# Inicializar partículas
x = np.random.uniform(0, 10, num_particles)
y = np.random.uniform(0, 10, num_particles)
vx = np.random.uniform(-0.5, 0.5, num_particles)
vy = np.random.uniform(-0.5, 0.5, num_particles)

# Matriz para armazenar trajetórias
trajectories_x = np.zeros((steps, num_particles))
trajectories_y = np.zeros((steps, num_particles))

# Botões de Controle
if st.sidebar.button("Iniciar Simulação"):
    st.write("Simulação iniciada!")

    # Criar gráfico animado
    fig, ax = plt.subplots()
    scatter = ax.scatter(x, y, s=50, alpha=0.7)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    # Função para atualizar as partículas
    def update(frame):
        global x, y, trajectories_x, trajectories_y, vx, vy
        x += vx
        y += vy
        x = np.clip(x, 0, 10)
        y = np.clip(y, 0, 10)
        scatter.set_offsets(np.c_[x, y])
        # Registrar trajetórias
        trajectories_x[frame, :] = x
        trajectories_y[frame, :] = y

    # Animação
    anim = FuncAnimation(fig, update, frames=steps, interval=100)
    st.pyplot(fig)

# Botão para Exportar Gráfico
if st.sidebar.button("Salvar Gráfico"):
    fig, ax = plt.subplots()
    for i in range(num_particles):
        ax.plot(trajectories_x[:, i], trajectories_y[:, i], alpha=0.5)  # Desenhar trajetórias
    ax.scatter(x, y, s=50, alpha=0.7, label="Posições Finais")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_title("Trajetórias das Partículas")
    ax.legend()
    # Salvar gráfico em buffer
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    st.download_button(
        label="Baixar Gráfico",
        data=buf,
        file_name="trajetorias_particulas.png",
        mime="image/png"
    )
