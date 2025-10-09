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
        self.setStyleSheet("background-color: #ffffff;")
        
        # Por ejemplo, una lista de materiales, botones para agregar/eliminar, etc.

        # self.material_list = QListWidget()
        # layout_material.addWidget(self.material_list)
        # self.add_button = QPushButton("Agregar Material")
        # layout_material.addWidget(self.add_button)
        # self.add_button.clicked.connect(self.agregar_material)
        
        # self.remove_button = QPushButton("Eliminar Material")
        # layout_material.addWidget(self.remove_button)
        # self.remove_button.clicked.connect(self.eliminar_material)
        
        # def agregar_material(self):
        #     Lógica para agregar un material
        #     pass
        # def eliminar_material(self):
        #     Lógica para eliminar un material
        #     pass
# Ventana de Materiales ejemplo
#class Materiales(QWidget):
#    def __init__(self):
#        super().__init__()
#        layout = QVBoxLayout()
#        layout.addWidget(QLabel("Página de Materiales"))
#        self.setLayout(layout)
#        self.setStyleSheet("background-color: #ffffff;")

#        # Aquí puedes agregar más widgets y funcionalidades específicas para la ventana de Materiales
#        # Por ejemplo, una lista de materiales, botones para agregar/eliminar, etc.
