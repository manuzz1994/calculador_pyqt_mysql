from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import pyqtSignal

class BarraLateral(QWidget):
    option_selected = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.setObjectName("BarraLateral")
        
        layout_izquierda = QVBoxLayout()
        layout_izquierda.setSpacing(10)
        layout_izquierda.setContentsMargins(10, 10, 10, 10)
        
        # Botones de la barra lateral - MÁS OPCIONES
        self.buttons = {
            "Calculadora": QPushButton("Calculadora"),
            "Materiales": QPushButton("Materiales"),
            "Envases": QPushButton("Envases"),
            "Costos Fijos": QPushButton("Costos Fijos"),
            "Recetas": QPushButton("Recetas")
        }
        
        for name, button in self.buttons.items():
            button.setObjectName("botonSidebar")
            button.setFixedHeight(40)
            button.clicked.connect(lambda checked, n=name: self.option_selected.emit(n))
            layout_izquierda.addWidget(button)
            
        layout_izquierda.addStretch()
        
        self.setLayout(layout_izquierda)