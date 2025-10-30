from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QHBoxLayout, QPushButton, QListWidgetItem, QInputDialog, QMessageBox
from PyQt5.QtCore import Qt
from database.consultas import obtener_envases, agregar_envase, actualizar_envase, eliminar_envase, obtener_envase_por_id, obtener_envase_por_tipo

class GestionEnvases(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.cargar_envases()

    def init_ui(self):
        layout = QVBoxLayout()
        
        titulo = QLabel("Gestión de Envases")
        titulo.setObjectName("tituloSeccion")
        layout.addWidget(titulo)
        
        self.lista_envases = QListWidget()
        layout.addWidget(self.lista_envases)

        layout_botones = QHBoxLayout()

        self.btn_agregar = QPushButton("Agregar")
        self.btn_editar = QPushButton("Editar")
        self.btn_eliminar = QPushButton("Eliminar")
        self.btn_actualizar = QPushButton("Actualizar")

        layout_botones.addWidget(self.btn_agregar)
        layout_botones.addWidget(self.btn_editar)
        layout_botones.addWidget(self.btn_eliminar)
        layout_botones.addWidget(self.btn_actualizar)

        layout.addLayout(layout_botones)
        self.setLayout(layout)

        self.btn_agregar.clicked.connect(self.agregar_envase)
        self.btn_editar.clicked.connect(self.editar_envase)
        self.btn_eliminar.clicked.connect(self.eliminar_envase)
        self.btn_actualizar.clicked.connect(self.cargar_envases)

    def cargar_envases(self):
        try:
            self.lista_envases.clear()
            envases = obtener_envases()
            for envase in envases:
                item = QListWidgetItem(f"{envase['nombre']} - ${envase['precio']} ({envase['tipo']})")
                item.setData(Qt.UserRole, envase['id'])
                self.lista_envases.addItem(item)
        except Exception as e:
            print(f"Error cargando envases: {e}")

    def agregar_envase(self):
        nombre, ok1 = QInputDialog.getText(self, "Agregar Envase", "Nombre del envase:")
        if not ok1 or not nombre.strip():
            return
            
        precio, ok2 = QInputDialog.getDouble(self, "Agregar Envase", "Precio del envase:", decimals=2)
        if not ok2:
            return
            
        tipos = ['vela', 'difusor']
        tipo, ok3 = QInputDialog.getItem(
            self, "Agregar Envase", "Tipo de envase:", 
            tipos, 0, False
        )
        if not ok3 or not tipo:
            return
        
        # 🔍 DEBUG: Ver qué valores se están enviando
        print(f"🔍 DEBUG - Nombre: {nombre}")
        print(f"🔍 DEBUG - Precio: {precio}") 
        print(f"🔍 DEBUG - Tipo: '{tipo}' (longitud: {len(tipo)})")
        
        try:
            resultado = agregar_envase(nombre, tipo, precio)
            if resultado is not None:
                QMessageBox.information(self, "Éxito", "Envase agregado correctamente.")
                self.cargar_envases()
            else:
                QMessageBox.critical(self, "Error", "No se pudo agregar el envase.")
        except Exception as e:
            print(f"❌ ERROR: {e}")
            QMessageBox.critical(self, "Error", f"Error al agregar envase: {e}")

    def editar_envase(self):
        envase_seleccionado = self.lista_envases.currentItem()
        if not envase_seleccionado:
            QMessageBox.warning(self, "Advertencia", "Seleccione un envase para editar.")
            return
        
        envase_id = envase_seleccionado.data(Qt.UserRole)
        envase_data = obtener_envase_por_id(envase_id)
        if not envase_data:
            QMessageBox.critical(self, "Error", "No se encontró el envase seleccionado")
            return  
        
        envase = envase_data[0]
        nombre, ok1 = QInputDialog.getText(self, "Editar Envase", "Nuevo nombre del envase:", text=envase['nombre'])
        if not ok1 or not nombre.strip():
            return
        
        precio, ok2 = QInputDialog.getDouble(self, "Editar Envase", "Nuevo precio del envase:", value=float(envase['precio']), decimals=2)
        if not ok2:
            return
        
        tipos = ['vela', 'difusor']
        tipo, ok3 = QInputDialog.getItem(self, "Editar Envase", "Nuevo tipo de envase:", tipos, current=tipos.index(envase['tipo']), editable=False)
        if not ok3 or not tipo:
            return
        
        resultado = actualizar_envase(envase_id, nombre, tipo, precio)
        if resultado is not None:
            QMessageBox.information(self, "Éxito", "Envase actualizado correctamente.")
            self.cargar_envases()
        else:
            QMessageBox.critical(self, "Error", "No se pudo actualizar el envase.")   

    def eliminar_envase(self):
        envase_seleccionado = self.lista_envases.currentItem()
        if not envase_seleccionado:
            QMessageBox.warning(self, "Advertencia", "Seleccione un envase para eliminar.")
            return
        
        envase_id = envase_seleccionado.data(Qt.UserRole)
      
        confirmacion = QMessageBox.question(
            self, "Confirmar Eliminación",
            "¿Está seguro de que desea eliminar este envase?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if confirmacion == QMessageBox.Yes:
            resultado = eliminar_envase(envase_id)
            if resultado is not None:
                QMessageBox.information(self, "Éxito", "Envase eliminado correctamente.")
                self.cargar_envases()
            else:
                QMessageBox.critical(self, "Error", "No se pudo eliminar el envase.")


