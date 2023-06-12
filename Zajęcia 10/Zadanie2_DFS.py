class Vertex:
    def __init__(self, label):
        self.label = label
        self.visited = False
        self.time_1 = 0
        self.time_2 = 0
        self.parent = None


def DFS(graph):
    for vertex in graph:
        vertex.visited = False
        vertex.parent = None

    time = 0

    for vertex in graph:
        if not vertex.visited:
            time = DFS_Explore(vertex, time)


def DFS_Explore(vertex, time):
    time += 1
    vertex.time_1 = time
    vertex.visited = True

    for neighbor in vertex.neighbors:
        if not neighbor.visited:
            neighbor.parent = vertex
            time = DFS_Explore(neighbor, time)

    time += 1
    vertex.time_2 = time

    return time


A = Vertex('A')
B = Vertex('B')
C = Vertex('C')
D = Vertex('D')
E = Vertex('E')
F = Vertex('F')

A.neighbors = [B, C]
B.neighbors = [A, D]
C.neighbors = [A, D, E]
D.neighbors = [B, C, F]
E.neighbors = [C, F]
F.neighbors = [D, E]

graph = [A, B, C, D, E, F]

DFS(graph)

for vertex in graph:
    print(f'Wierzchołek {vertex.label}: czas 1 - {vertex.time_1}, czas 2 - {vertex.time_2}')