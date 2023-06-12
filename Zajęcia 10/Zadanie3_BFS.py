def BFS(graph, source):
    visited = [False] * len(graph)
    distance = [-1] * len(graph)
    parent = [-1] * len(graph)

    visited[source] = True
    distance[source] = 0

    queue = [source]
    queue_index = 0

    while queue_index < len(queue):
        u = queue[queue_index]
        queue_index += 1

        for v in range(len(graph)):
            if graph[u][v] == 1 and not visited[v]:
                visited[v] = True
                distance[v] = distance[u] + 1
                parent[v] = u
                queue.append(v)

    return distance, parent


graph = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0]
]

source_vertex = 0
distances, parents = BFS(graph, source_vertex)

for vertex in range(len(graph)):
    print(f'Wierzchołek {vertex}: odległość - {distances[vertex]}, poprzednik - {parents[vertex]}')