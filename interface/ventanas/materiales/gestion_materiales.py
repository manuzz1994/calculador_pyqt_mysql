"""
Listar materia prima desde la base de datos con botones para el CRUD de materia prima.
"""
# interface/ventanas/materiales/gestion_materiales.py
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QListWidget, QListWidgetItem, QPushButton, 
                             QMessageBox)
from PyQt5.QtCore import Qt
from database.consultas import obtener_materias_primas

class GestionMateriales(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.cargar_materiales()
    
    def init_ui(self):
        # PASO 3: Crear el layout principal
        layout = QVBoxLayout()
        
        # PASO 1: Agregar título
        titulo = QLabel("Gestión de Materia Prima")
        titulo.setObjectName("tituloSeccion")
        layout.addWidget(titulo)
        
        # PASO 1: Agregar lista de materiales
        self.lista_materiales = QListWidget()
        layout.addWidget(self.lista_materiales)
        
        # PASO 1 y 3: Agregar botones en layout horizontal
        layout_botones = QHBoxLayout()
        
        # PASO 2: Crear botones para cada operación CRUD
        self.btn_agregar = QPushButton("Agregar")
        self.btn_editar = QPushButton("Editar") 
        self.btn_eliminar = QPushButton("Eliminar")
        self.btn_actualizar = QPushButton("Actualizar")
        
        # Agregar botones al layout horizontal
        layout_botones.addWidget(self.btn_agregar)
        layout_botones.addWidget(self.btn_editar)
        layout_botones.addWidget(self.btn_eliminar) 
        layout_botones.addWidget(self.btn_actualizar)
        
        # Agregar el layout de botones al principal
        layout.addLayout(layout_botones)
        
        self.setLayout(layout)

        # Conectar botones a sus funciones
        self.btn_agregar.clicked.connect(self.agregar_material)
        #self.btn_editar.clicked.connect(self.editar_material)
        #self.btn_eliminar.clicked.connect(self.eliminar_material)
        self.btn_actualizar.clicked.connect(self.cargar_materiales)

    # CARGAR MATERIALES
    def cargar_materiales(self):
        try:
            self.lista_materiales.clear()
            materiales = obtener_materias_primas()
            for material in materiales:
                item = QListWidgetItem(f"{material['id']}: {material['nombre']} - ${material['precio_por_gramo']}/g - Tipo: {material['tipo']}")
                item.setData(Qt.UserRole, material['id'])
                self.lista_materiales.addItem(item)
            else:
                self.lista_materiales.addItem("No hay materiales registrados.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudieron cargar los materiales: {e}")

    # FUNCIONES DE BOTONES
    def agregar_material(self):
        """PASO 2: Función para agregar nuevo material"""
        # PASO 5: Usar QInputDialog para pedir datos al usuario

        # Tip: Puedes usar QInputDialog.getText(), getDouble(), getItem()
        
        # 1. Pedir nombre del material
        
        # 2. Pedir precio por gramo  
        
        # 3. Pedir tipo (de una lista predefinida)
        
        # 4. PASO 4: Llamar a crear_materia_prima() con los datos
        
        # 5. PASO 5: Mostrar mensaje de éxito/error y recargar lista

        pass