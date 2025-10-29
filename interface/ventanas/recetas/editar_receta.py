# interface/ventanas/recetas/editar_receta.py
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel

class EditarReceta(QDialog):
    def __init__(self, receta_id=None, modo="edicion", parent=None):
        super().__init__(parent)
        print("✅ EditarReceta inicializado")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Editor de Recetas - En desarrollo"))
        self.setLayout(layout)