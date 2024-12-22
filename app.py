import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Configuração do Título
st.title("Simulação de IA para Nanotecnologia - Anna Dalmoneki")
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
        global x, y, vx, vy  # Declara as variáveis como globais
        x += vx
        y += vy
        x = np.clip(x, 0, 10)
        y = np.clip(y, 0, 10)
        scatter.set_offsets(np.c_[x, y])

    # Animação
    anim = FuncAnimation(fig, update, frames=steps, interval=100)

    st.pyplot(fig)

if st.sidebar.button("Resetar Simulação"):
    st.write("Simulação resetada!")
    # Reiniciar partículas
    x = np.random.uniform(0, 10, num_particles)
    y = np.random.uniform(0, 10, num_particles)
