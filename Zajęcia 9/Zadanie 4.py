class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, source, destination, weight):
        self.adj_list[source].append((destination, weight))
        self.adj_list[destination].append((source, weight))

    def dijkstra(self, source):
        distances = [float('inf')] * self.num_vertices
        distances[source] = 0
        visited = [False] * self.num_vertices

        for _ in range(self.num_vertices - 1):
            min_dist = float('inf')
            min_vertex = -1

            for v in range(self.num_vertices):
                if not visited[v] and distances[v] < min_dist:
                    min_dist = distances[v]
                    min_vertex = v

            if min_vertex == -1:
                break

            visited[min_vertex] = True

            for neighbor, weight in self.adj_list[min_vertex]:
                distance = distances[min_vertex] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance

        return distances


def build_graph():
    print("Witaj w programie do budowania grafu i wyznaczania najkrótszej drogi!")
    graph_type = input("Podaj typ grafu (skierowany, nieskierowany, ważony, inny możliwy): ")

    num_vertices = int(input("Podaj ilość wierzchołków: "))
    graph = Graph(num_vertices)

    num_edges = int(input("Podaj ilość połączeń: "))

    for _ in range(num_edges):
        source = int(input("Podaj początek połączenia (wierzchołek źródłowy): "))
        destination = int(input("Podaj koniec połączenia (wierzchołek docelowy): "))
        weight = int(input("Podaj wagę połączenia: "))
        graph.add_edge(source, destination, weight)

    source_vertex = int(input("Podaj wierzchołek początkowy dla algorytmu Dijkstry: "))
    distances = graph.dijkstra(source_vertex)

    print("Najkrótsze odległości od wierzchołka", source_vertex)
    for vertex in range(graph.num_vertices):
        print(f"Do wierzchołka {vertex}: {distances[vertex]}")


build_graph()