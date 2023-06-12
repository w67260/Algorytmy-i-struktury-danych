def prim(graph):
    mst = {}
    visited = set()
    edges = []

    start_vertex = 'A'
    visited.add(start_vertex)

    for neighbor, weight in graph[start_vertex]:
        edges.append((start_vertex, neighbor, weight))

    while edges:
        edges.sort(key=lambda x: x[2])
        u, v, weight = edges.pop(0)

        if v not in visited:
            if u not in mst:
                mst[u] = []
            mst[u].append((v, weight))
            visited.add(v)

            for neighbor, weight in graph[v]:
                edges.append((v, neighbor, weight))

    return mst


graph = {
    'A': [('B', 1), ('E', 4), ('F', 8)],
    'B': [('A', 1), ('C', 2), ('F', 6), ('G', 6)],
    'C': [('B', 2), ('D', 3), ('G', 2)],
    'D': [('C', 3), ('G', 1), ('H', 4)],
    'E': [('A', 4), ('F', 5)],
    'F': [('A', 8), ('B', 6), ('E', 5), ('G', 1)],
    'G': [('B', 6), ('C', 2), ('D', 1), ('F', 1), ('H', 1)],
    'H': [('D', 4), ('G', 1)]
}

mst = prim(graph)

for vertex in mst:
    for neighbor, weight in mst[vertex]:
        print(f'({vertex}, {neighbor}, {weight})')