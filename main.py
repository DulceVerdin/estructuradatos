'''
from estructuras.no_lineales.graph import Graph


def test_graph():
    graph = Graph()

    # Agregar vértices
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")

    # Agregar arcos
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")

    # 1. Mostrar Vértices
    print("Vértices:")
    print(graph.get_vertices())

    # 2. Mostrar Lista de adyacencia
    print("\nLista de adyacencia:")
    for vertex, adjacent_vertices in graph.get_adjacency_list().items():
        adjacent_text = (
            ", ".join(adjacent_vertices)
            if adjacent_vertices
            else "Sin conexiones"
        )
        print(f"{vertex}: {adjacent_text}")

    # 3. Mostrar Matriz de adyacencia
    print("\nMatriz de adyacencia:")
    vertices, matrix = graph.get_adjacency_matrix()
    print("  " + " ".join(vertices))
    for index, row in enumerate(matrix):
        values = " ".join(str(value) for value in row)
        print(f"{vertices[index]} {values}")

    # 4. Mostrar Lista de arcos
    print("\nLista de arcos:")
    for vertex1, vertex2 in graph.get_edges():
        print(f"({vertex1}, {vertex2})")


if __name__ == "__main__":
    test_graph()
'''
import sys

from PySide6.QtWidgets import QApplication

from load.load_graph_gui import GraphController


def main():
	app = QApplication(sys.argv)

	controller = GraphController()
	controller.show()

	return app.exec()


if __name__ == "__main__":
	sys.exit(main())