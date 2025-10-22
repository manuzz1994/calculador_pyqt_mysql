from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QStackedWidget, QHBoxLayout
from interface.barra_lateral import BarraLateral
from interface.ventanas.calcu_ventana import CalcuVentana
# Importar las nuevas ventanas modulares
from interface.ventanas.materiales.gestion_materiales import GestionMateriales
from interface.ventanas.materiales.gestion_envases import GestionEnvases
from interface.ventanas.materiales.gestion_costos_fijos import GestionCostosFijos
from interface.ventanas.recetas.lista_recetas import ListaRecetas

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Calculadora de Recetas")
        self.setGeometry(100, 100, 800, 600)
        self.setObjectName("VentanaPrincipal")
        
        # Contenedor principal
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
        self.gestion_materiales = GestionMateriales()
        #self.gestion_envases = GestionEnvases()
        #self.gestion_costos_fijos = GestionCostosFijos()
        #self.lista_recetas = ListaRecetas()
        
        # Agregar todas las ventanas al stacked widget
        self.ventanas.addWidget(self.calcu_ventana)
        self.ventanas.addWidget(self.gestion_materiales)
        #self.ventanas.addWidget(self.gestion_envases)
        #self.ventanas.addWidget(self.gestion_costos_fijos)
        #self.ventanas.addWidget(self.lista_recetas)
        
        # Mostrar la ventana de cálculo por defecto
        self.ventanas.setCurrentWidget(self.calcu_ventana)
        
    def cambiar_ventana(self, opcion):
        if opcion == "Calculadora":
            self.ventanas.setCurrentWidget(self.calcu_ventana)
        elif opcion == "Materiales":
            self.ventanas.setCurrentWidget(self.gestion_materiales)
        elif opcion == "Envases":
            #self.ventanas.setCurrentWidget(self.gestion_envases)
            pass
        elif opcion == "Costos Fijos":
            #self.ventanas.setCurrentWidget(self.gestion_costos_fijos)
            pass
        elif opcion == "Recetas":
            #self.ventanas.setCurrentWidget(self.lista_recetas)
            pass
        else:
            print("Opción no reconocida")