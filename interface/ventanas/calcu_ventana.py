from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
"""
En esta ventana se implementará la calculadora de recetas.
En la cual se podrá elegir una receta, ingresar las cantidades utilizadas, materiales utilizados
y obtener el costo total de la receta con sus respectivos materiales detallados.
Atraves de un pequeño formulario el usuario podrá ingresar los datos necesarios para realizar el cálculo.
También se podrá elegir entre las 4 recetas disponibles.
"""

# Ventana de la Calculadora
class CalcuVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("SeccionPrincipal")
        
        layout_calculadora = QVBoxLayout()
        layout_calculadora.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        
        titulo = QLabel("Calculadora")
        titulo.setObjectName("tituloPrincipal")
        layout_calculadora.addWidget(titulo)
        
        
        
        self.setLayout(layout_calculadora)
        