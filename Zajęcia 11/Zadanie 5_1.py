def prim(graph):
    mst = {}
    visited = set()
    edges = []

    start_vertex = list(graph.keys())[0]
    visited.add(start_vertex)

    for neighbor, weight in graph[start_vertex]:
        edges.append((start_vertex, neighbor, weight))

    while len(mst) < len(graph) - 1:
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





