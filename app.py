# Simulação com Clusters
if st.sidebar.button("Agrupar em Clusters"):
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
