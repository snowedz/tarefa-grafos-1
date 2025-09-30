import os
import numpy as np
import pandas as pd

# 1º questão

with open(os.path.join(os.path.dirname(__file__), 'graph1.txt'), 'r') as f:
    lines = f.readlines()
num_vertices, num_edges = map(int, lines[0].strip().split())
graph = {i: {} for i in range(num_vertices)}
for line in lines[1:num_edges + 1]:
    u, v, cost = map(int, line.strip().split())
    u = u - 1  
    v = v - 1  
    graph[u][v] = cost
    graph[v][u] = cost 
    
matriz_adj = np.zeros((num_vertices, num_vertices))
for i in range(num_vertices):
    for j in graph[i]:
        matriz_adj[i][j] = graph[i][j]
    matriz_adj[i][i] = 0 # Distancia de um vértice para ele mesmo é 0
    for j in range(num_vertices):
        if matriz_adj[i][j] == 0 and i != j:
            matriz_adj[i][j] = np.inf # Distancia infinita se não há aresta
dist_matriz = matriz_adj.copy()

# algoritmo de Floyd-Warshall
# se D[i,j] > D[i,k] + D[k,j] então a menor distância entre i e j é passando por k
for k in range(num_vertices):
    for i in range(num_vertices):
        for j in range(num_vertices):
            if dist_matriz[i][j] > dist_matriz[i][k] + dist_matriz[k][j]: # Se passar por k for melhor
                dist_matriz[i][j] = dist_matriz[i][k] + dist_matriz[k][j] # Atualiza a distância

soma_dist = dist_matriz.sum(axis=1)
vertice_central = np.argmin(soma_dist)
dist_centro = dist_matriz[vertice_central]
vertice_distante = np.argmax(dist_centro)
maior_dist = dist_centro[vertice_distante]
print("1º questão:")
print(f"Vértice central: {vertice_central + 1}")
print(f"Distâncias da estação central até os demais vértices: {dist_centro}")
print(f"Vértice mais distante da estação central: {vertice_distante} com distância {maior_dist}")
print("Matriz de distâncias mínimas entre todos os pares de vértices:")
df = pd.DataFrame(dist_matriz)
print(df)

# 2º Questão
def bellman_ford(vertices, edges_df, source):
    """
    Implementação do Bellman-Ford usando numpy e pandas.
    """
    # --- Inicialização (pseudocódigo: d[v] ← ∞, π[v] ← NIL) ---
    dist = np.full(vertices, np.inf)   # vetor de distâncias
    dist[source] = 0
    predecessor = np.full(vertices, -1)  # vetor de predecessores

    # --- Relaxamento (pseudocódigo: para i de 1 até |V|-1) ---
    for _ in range(vertices - 1):
        for _, edge in edges_df.iterrows():
            u, v, w = edge["u"], edge["v"], edge["w"]
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                predecessor[v] = u

    # --- Verificação de ciclos negativos ---
    for _, edge in edges_df.iterrows():
        u, v, w = edge["u"], edge["v"], edge["w"]
        if dist[u] + w < dist[v]:
            raise ValueError("Grafo contém ciclo negativo!")

    return dist, predecessor


def get_path(predecessor, target):
    """
    Reconstrói o caminho mínimo a partir do vetor predecessor (π[v]).
    """
    path = []
    while target != -1:
        path.insert(0, target)
        target = int(predecessor[target])
    return path

file_path = os.path.join(os.getcwd(), "graph2.txt")

# Primeira linha: número de vértices e arestas
with open(file_path, "r") as f:
    header = f.readline().strip()
    V, E = map(int, header.split())

# Demais linhas: arestas
edges_df = pd.read_csv(
    file_path, 
    sep="\t", 
    skiprows=1, 
    names=["u", "v", "w"]
)

print("Grafo carregado:")
print(edges_df)

source, target = 0, 6
dist, pred = bellman_ford(V, edges_df, source)
path = get_path(pred, target)

print("\nResultado:")
print("Caminho mínimo:", path)
print("Custo total:", dist[target], "Wh")


