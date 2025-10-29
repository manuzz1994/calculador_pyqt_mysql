from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class GestionEnvases(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Gestión de Envases - En desarrollo"))
        self.setLayout(layout)