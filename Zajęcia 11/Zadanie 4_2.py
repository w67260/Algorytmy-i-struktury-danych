def find(parent, vertex):
    if parent[vertex] == vertex:
        return vertex
    return find(parent, parent[vertex])

def union(parent, rank, vertex1, vertex2):
    root1 = find(parent, vertex1)
    root2 = find(parent, vertex2)

    if rank[root1] < rank[root2]:
        parent[root1] = root2
    elif rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root2] = root1
        rank[root1] += 1

def kruskal(graph):
    mst = []
    edges = []

    parent = {}
    rank = {}
    for vertex in graph:
        parent[vertex] = vertex
        rank[vertex] = 0

    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            edges.append((vertex, neighbor, weight))

    edges.sort(key=lambda x: x[2])

    while len(mst) < len(graph) - 1:
        if len(edges) == 0:
            break

        u, v, weight = edges.pop(0)

        if find(parent, u) != find(parent, v):
            mst.append((u, v, weight))
            union(parent, rank, u, v)

    return mst