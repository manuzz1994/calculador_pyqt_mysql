from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class GestionCostosFijos(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Gestión de Costos Fijos - En desarrollo"))
        self.setLayout(layout)