class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, source, destination, weight=1):
        self.adj_matrix[source][destination] = weight

    def display_adj_matrix(self):
        print("Macierz sąsiedztwa:")
        for row in self.adj_matrix:
            print(row)

    def display_adj_list(self):
        print("Lista sąsiedztwa:")
        for vertex in range(self.num_vertices):
            neighbors = [dest for dest, weight in enumerate(self.adj_matrix[vertex]) if weight != 0]
            print(f"Wierzchołek {vertex}: {neighbors}")

    def display_graph(self):
        print("Interpretacja graficzna:")
        for source in range(self.num_vertices):
            for dest, weight in enumerate(self.adj_matrix[source]):
                if weight != 0:
                    print(f"{source} ---{weight}---> {dest}")


def build_graph():
    print("Witaj w programie do budowania grafu!")
    graph_type = input("Podaj typ grafu (skierowany, nieskierowany, ważony, inny możliwy): ")

    num_vertices = int(input("Podaj ilość wierzchołków: "))
    graph = Graph(num_vertices)

    num_edges = int(input("Podaj ilość połączeń: "))

    for i in range(num_edges):
        source = int(input("Podaj początek połączenia (wierzchołek źródłowy): "))
        destination = int(input("Podaj koniec połączenia (wierzchołek docelowy): "))
        weight = int(input("Podaj wagę połączenia (jeśli graf jest nieważony, wpisz 1): "))
        graph.add_edge(source, destination, weight)

    print("\nGraf został zdefiniowany:")
    graph.display_adj_matrix()
    print()
    graph.display_adj_list()
    print()
    graph.display_graph()


build_graph()