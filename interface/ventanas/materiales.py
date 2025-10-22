import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

"""
En esta ventana se implementará la gestión de materiales.
Aquí se podrán agregar, eliminar y modificar los materiales disponibles,
así como ver detalles como el costo por unidad.

"""

class Materiales(QWidget):
    def __init__(self):
        super().__init__()
        layout_material = QVBoxLayout()
        layout_material.addWidget(QLabel("Página de Materiales"))
        self.setLayout(layout_material)
        

