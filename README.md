# Atividade de Grafos 

## Alunos [Luiz Eduardo Neves de Sousa](https://github.com/snowedz) e [Wictor Oliveira Soares de Lima](https://github.com/WictorSoares6)

Linguagem: Python

Bibliotecas utilizadas: OS, Numpy, Pandas e Heapq


Na primeira questão foi escolhido o algorítimo de Floyd-Warshall pois a questão necessita saber o cálculo do caminho minimo entre todos os pares de vertices
e este algorítimo consegue fazer isso da forma mais eficiente.

se D[i,j] > D[i,k] + D[k,j] então a menor distância entre i e j é passando por k
for k in range(num_vertices):
    for i in range(num_vertices):
        for j in range(num_vertices):
            if dist_matriz[i][j] > dist_matriz[i][k] + dist_matriz[k][j]: # Se passar por k for melhor
                dist_matriz[i][j] = dist_matriz[i][k] + dist_matriz[k][j] # Atualiza a distância


Na segunda questão ...


Na terceira questão foi escolhido o algorítimo de Dijkstra pois é necessário calcular o menor caminho entre uma origem e um destino.
    while pq: 
        dist_atual, (r, c) = heapq.heappop(pq)
        if (r, c) == objetivo: -> Ao chegar no destino, o loop para
            break
        if dist_atual > dist[r, c]:
            continue
        for dr, dc in direcao: -> na posição atual, olha para todas as direções
            nr, nc = r + dr, c + dc
            if 0 <= nr < linhas and 0 <= nc < colunas:
                alt = dist_atual + grid[nr, nc]
                if alt < dist[nr, nc]:  -> se o caminho alternativo for de menor custo
                    dist[nr, nc] = alt -> atualiza a distancia
                    prev[(nr, nc)] = (r, c) -> coloca o caminho atual como parte do caminho mais curto
                    heapq.heappush(pq, (alt, (nr, nc)))
