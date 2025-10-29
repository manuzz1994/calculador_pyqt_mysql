from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class EditaReceta(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Editar Recetas - En desarrollo"))
        self.setLayout(layout)