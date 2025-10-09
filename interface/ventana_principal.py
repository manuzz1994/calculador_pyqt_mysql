from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QStackedWidget, QHBoxLayout
from interface.barra_lateral import BarraLateral
from interface.ventanas.calcu_ventana import CalcuVentana
from interface.ventanas.materiales import Materiales
from interface.ventanas.recetas import Recetas

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Calculadora de Recetas")
        self.setGeometry(100, 100, 800, 600)
        self.setObjectName("VentanaPrincipal")
        
        #Contenedor principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        principal_layout = QHBoxLayout()
        central_widget.setLayout(principal_layout)
        
        
        # Barra lateral
        self.barra_lateral = BarraLateral()
        self.barra_lateral.option_selected.connect(self.cambiar_ventana)
        principal_layout.addWidget(self.barra_lateral)
        
        # Área de ventanas intercambiables
        self.ventanas = QStackedWidget()
        principal_layout.addWidget(self.ventanas, 1)
        
        # Ventanas individuales
        self.calcu_ventana = CalcuVentana()
        self.materiales = Materiales()
        self.recetas = Recetas()
        
        self.ventanas.addWidget(self.calcu_ventana)
        self.ventanas.addWidget(self.materiales)
        self.ventanas.addWidget(self.recetas)
        
        # Mostrar la ventana de cálculo por defecto
        self.ventanas.setCurrentWidget(self.calcu_ventana)
        
    def cambiar_ventana(self, opcion):
        if opcion == "Calculadora":
            self.ventanas.setCurrentWidget(self.calcu_ventana)
        elif opcion == "Materiales":
            self.ventanas.setCurrentWidget(self.materiales)
        elif opcion == "Recetas":
            self.ventanas.setCurrentWidget(self.recetas)
        else:
            print("Opción no reconocida")