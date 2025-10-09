from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import pyqtSignal

class BarraLateral(QWidget):
    option_selected = pyqtSignal(str) # Señal personalizada para comunicar la opción seleccionada
    
    def __init__(self):
        super().__init__()
        self.setObjectName("BarraLateral") # Estilo específico para la barra lateral
        
        
        layout_izquierda = QVBoxLayout()
        layout_izquierda.setSpacing(10) # Espacio entre botones
        layout_izquierda.setContentsMargins(10, 10, 10, 10) # Márgenes alrededor del layout
        
        
        # Botones de la barra lateral
        self.buttons = {
            "Calculadora": QPushButton("Calculadora"),
            "Materiales": QPushButton("Materiales"),
            "Recetas": QPushButton("Recetas")
        }
        
        for name, button in self.buttons.items():
            button.setObjectName("botonSidebar")  # Estilo específico para los botones de la barra lateral
            button.setFixedHeight(40)
            button.clicked.connect(lambda checked, n=name: self.option_selected.emit(n))
            layout_izquierda.addWidget(button)
            
        layout_izquierda.addStretch() # Empuja los botones hacia arriba
        
        self.setLayout(layout_izquierda)
        
        
    