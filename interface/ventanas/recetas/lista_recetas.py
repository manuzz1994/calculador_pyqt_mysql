from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class ListaRecetas(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Lista de Recetas - En desarrollo"))
        self.setLayout(layout)