import math

from PySide6.QtCore import QFile, Qt
from PySide6.QtGui import QBrush, QColor, QFont, QPainter, QPen
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (
    QAbstractItemView,
    QComboBox,
    QGraphicsEllipseItem,
    QGraphicsLineItem,
    QGraphicsScene,
    QGraphicsTextItem,
    QGraphicsView,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPlainTextEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
)

from estructuras.no_lineales.graph import Graph


class GraphController:
    """Controlador para la interfaz de grafos no dirigidos."""

    def __init__(self):
        loader = QUiLoader()
        ui_file = QFile("ui/interfaz_grafo.ui")
        if not ui_file.open(QFile.ReadOnly):
            raise RuntimeError("No se pudo abrir ui/interfaz_grafo.ui")

        self.window = loader.load(ui_file)
        ui_file.close()

        if self.window is None:
            raise RuntimeError("No se pudo cargar ui/interfaz_grafo.ui")

        self.graph = Graph()
        self.scene = QGraphicsScene(self.window)

        self._bind_widgets()

        self.graphicsViewGraph.setScene(self.scene)
        self.graphicsViewGraph.setRenderHint(QPainter.Antialiasing, True)
        self.graphicsViewGraph.setRenderHint(QPainter.TextAntialiasing, True)

        self._configure_read_only_widgets()
        self._connect_signals()
        self._refresh_all_views()

    def show(self):
        self.window.show()

    def _bind_widgets(self):
        self.txtVertex = self.window.findChild(QLineEdit, "txtVertex")
        self.btnAddVertex = self.window.findChild(QPushButton, "btnAddVertex")
        self.cmbVertex = self.window.findChild(QComboBox, "cmbVertex")
        self.btnDeleteVertex = self.window.findChild(QPushButton, "btnDeleteVertex")

        self.cmbOrigin = self.window.findChild(QComboBox, "cmbOrigin")
        self.cmbDestination = self.window.findChild(QComboBox, "cmbDestination")
        self.btnAddEdge = self.window.findChild(QPushButton, "btnAddEdge")
        self.btnDeleteEdge = self.window.findChild(QPushButton, "btnDeleteEdge")

        self.graphicsViewGraph = self.window.findChild(QGraphicsView, "graphicsViewGraph")
        self.btnRedrawGraph = self.window.findChild(QPushButton, "btnRedrawGraph")

        self.tblAdjacencyMatrix = self.window.findChild(QTableWidget, "tblAdjacencyMatrix")
        self.txtAdjacencyList = self.window.findChild(QPlainTextEdit, "txtAdjacencyList")
        self.tblEdges = self.window.findChild(QTableWidget, "tblEdges")

        self.lblGraphStatus = self.window.findChild(QLabel, "lblGraphStatus")
        self.btnClearGraph = self.window.findChild(QPushButton, "btnClearGraph")

        required_widgets = [
            self.txtVertex,
            self.btnAddVertex,
            self.cmbVertex,
            self.btnDeleteVertex,
            self.cmbOrigin,
            self.cmbDestination,
            self.btnAddEdge,
            self.btnDeleteEdge,
            self.graphicsViewGraph,
            self.btnRedrawGraph,
            self.tblAdjacencyMatrix,
            self.txtAdjacencyList,
            self.tblEdges,
            self.lblGraphStatus,
            self.btnClearGraph,
        ]
        if any(widget is None for widget in required_widgets):
            raise RuntimeError("Faltan widgets obligatorios en interfaz_grafo.ui")

    def _configure_read_only_widgets(self):
        self.tblAdjacencyMatrix.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tblEdges.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.txtAdjacencyList.setReadOnly(True)

    def _connect_signals(self):
        self.btnAddVertex.clicked.connect(self.add_vertex)
        self.btnDeleteVertex.clicked.connect(self.delete_vertex)
        self.btnAddEdge.clicked.connect(self.add_edge)
        self.btnDeleteEdge.clicked.connect(self.delete_edge)
        self.btnClearGraph.clicked.connect(self.clear_graph)
        self.btnRedrawGraph.clicked.connect(self.redraw_graph)

    def _refresh_all_views(self):
        self._refresh_vertex_selectors()
        self._refresh_adjacency_matrix()
        self._refresh_adjacency_list()
        self._refresh_edges_table()
        self._refresh_status_label()
        self.redraw_graph()

    def _refresh_vertex_selectors(self):
        vertices = self.graph.get_vertices()
        self.cmbVertex.clear()
        self.cmbOrigin.clear()
        self.cmbDestination.clear()
        self.cmbVertex.addItems(vertices)
        self.cmbOrigin.addItems(vertices)
        self.cmbDestination.addItems(vertices)

    def _refresh_adjacency_matrix(self):
        vertices, matrix = self.graph.get_adjacency_matrix()
        size = len(vertices)

        self.tblAdjacencyMatrix.clear()
        self.tblAdjacencyMatrix.setRowCount(size)
        self.tblAdjacencyMatrix.setColumnCount(size)
        self.tblAdjacencyMatrix.setHorizontalHeaderLabels(vertices)
        self.tblAdjacencyMatrix.setVerticalHeaderLabels(vertices)

        for row_index, row_values in enumerate(matrix):
            for column_index, value in enumerate(row_values):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                self.tblAdjacencyMatrix.setItem(row_index, column_index, item)

    def _refresh_adjacency_list(self):
        adjacency_list = self.graph.get_adjacency_list()
        lines = []
        for vertex in sorted(adjacency_list.keys()):
            neighbors = ", ".join(adjacency_list[vertex])
            lines.append(f"{vertex}: [{neighbors}]")

        if lines:
            self.txtAdjacencyList.setPlainText("\n".join(lines))
        else:
            self.txtAdjacencyList.setPlainText("")

    def _refresh_edges_table(self):
        edges = self.graph.get_edges()
        self.tblEdges.setRowCount(len(edges))

        for row_index, (vertex1, vertex2) in enumerate(edges):
            item_vertex1 = QTableWidgetItem(vertex1)
            item_vertex2 = QTableWidgetItem(vertex2)
            item_vertex1.setTextAlignment(Qt.AlignCenter)
            item_vertex2.setTextAlignment(Qt.AlignCenter)
            self.tblEdges.setItem(row_index, 0, item_vertex1)
            self.tblEdges.setItem(row_index, 1, item_vertex2)

    def _refresh_status_label(self):
        self.lblGraphStatus.setText(
            f"Vértices: {self.graph.vertex_count()} | Arcos: {self.graph.edge_count()}"
        )

    def _refresh_and_report(self, message):
        self._refresh_all_views()
        self.lblGraphStatus.setToolTip(message)

    def add_vertex(self):
        vertex = self.txtVertex.text().strip()
        if not vertex:
            QMessageBox.warning(self.window, "Dato requerido", "Ingresa un nombre de vértice.")
            return

        try:
            was_added = self.graph.add_vertex(vertex)
        except ValueError as exc:
            QMessageBox.warning(self.window, "Error", str(exc))
            return

        if was_added:
            self.txtVertex.clear()
            self._refresh_and_report("Vértice agregado.")
        else:
            QMessageBox.information(self.window, "Sin cambios", "El vértice ya existe.")

    def delete_vertex(self):
        vertex = self.cmbVertex.currentText().strip()
        if not vertex:
            return

        if self.graph.remove_vertex(vertex):
            self._refresh_and_report("Vértice eliminado.")

    def add_edge(self):
        origin = self.cmbOrigin.currentText().strip()
        destination = self.cmbDestination.currentText().strip()
        if not origin or not destination:
            QMessageBox.warning(
                self.window,
                "Datos requeridos",
                "Selecciona los dos vértices para crear el arco.",
            )
            return

        try:
            was_added = self.graph.add_edge(origin, destination)
        except ValueError as exc:
            QMessageBox.warning(self.window, "Error", str(exc))
            return

        if was_added:
            self._refresh_and_report("Arco agregado.")
        else:
            QMessageBox.information(self.window, "Sin cambios", "El arco ya existe.")

    def delete_edge(self):
        origin = self.cmbOrigin.currentText().strip()
        destination = self.cmbDestination.currentText().strip()
        if not origin or not destination:
            return

        if self.graph.remove_edge(origin, destination):
            self._refresh_and_report("Arco eliminado.")

    def clear_graph(self):
        self.graph.clear()
        self._refresh_and_report("Grafo limpiado.")

    def redraw_graph(self):
        self.scene.clear()
        vertices = self.graph.get_vertices()
        if not vertices:
            return

        center_x = 260
        center_y = 200
        radius = max(120, 40 * len(vertices))
        vertex_radius = 18

        positions = {}
        angle_step = (2 * math.pi) / len(vertices)
        for index, vertex in enumerate(vertices):
            angle = angle_step * index
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            positions[vertex] = (x, y)

        line_pen = QPen(QColor("#D4AF37"))
        line_pen.setWidth(2)

        for vertex1, vertex2 in self.graph.get_edges():
            x1, y1 = positions[vertex1]
            x2, y2 = positions[vertex2]
            line_item = QGraphicsLineItem(x1, y1, x2, y2)
            line_item.setPen(line_pen)
            self.scene.addItem(line_item)

        node_pen = QPen(QColor("#F5D76E"))
        node_pen.setWidth(2)
        node_brush = QBrush(QColor("#1E1E1E"))

        for vertex, (x, y) in positions.items():
            ellipse_item = QGraphicsEllipseItem(
                x - vertex_radius,
                y - vertex_radius,
                vertex_radius * 2,
                vertex_radius * 2,
            )
            ellipse_item.setPen(node_pen)
            ellipse_item.setBrush(node_brush)
            self.scene.addItem(ellipse_item)

            text_item = QGraphicsTextItem(vertex)
            text_item.setFont(QFont("Segoe UI", 9, QFont.Bold))
            text_item.setDefaultTextColor(QColor("#F5E6B3"))
            text_rect = text_item.boundingRect()
            text_item.setPos(x - text_rect.width() / 2, y - text_rect.height() / 2)
            self.scene.addItem(text_item)

        self.scene.setSceneRect(self.scene.itemsBoundingRect().adjusted(-40, -40, 40, 40))

