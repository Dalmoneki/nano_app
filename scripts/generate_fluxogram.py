from graphviz import Digraph

# Criando o fluxograma
dot = Digraph()

# Entrada
dot.node("Entrada", "Entrada\n- Número de Partículas\n- Configurações Iniciais")
dot.node("Processamento", "Processamento\n- Movimento das Partículas\n- Treinamento com IA")
dot.node("Saída", "Saída\n- Gráficos\n- Dados Exportados")

# Conexões
dot.edges([("Entrada", "Processamento"), ("Processamento", "Saída")])

# Salvar o fluxograma
dot.render("fluxograma_simulacao", format="png", cleanup=True)
