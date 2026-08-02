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