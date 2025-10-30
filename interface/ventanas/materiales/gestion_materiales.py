"""
Listar materia prima desde la base de datos con botones para el CRUD de materia prima.
"""
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QListWidget, QListWidgetItem, QPushButton, QMessageBox, QInputDialog
from PyQt5.QtCore import Qt
from database.consultas import obtener_materia_prima, agregar_materia_prima, actualizar_materia_prima, eliminar_materia_prima, obtener_materia_prima_id, verificar_material_en_uso

class GestionMateriales(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.cargar_materiales()
    
    def init_ui(self):
        layout = QVBoxLayout()
        
        titulo = QLabel("Gestión de Materia Prima")
        titulo.setObjectName("tituloSeccion")
        layout.addWidget(titulo)
        
        self.lista_materiales = QListWidget()
        layout.addWidget(self.lista_materiales)
        
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

        self.btn_agregar.clicked.connect(self.agregar_material)
        self.btn_editar.clicked.connect(self.editar_material)
        self.btn_eliminar.clicked.connect(self.eliminar_material)
        self.btn_actualizar.clicked.connect(self.cargar_materiales)


    def cargar_materiales(self):
        try:
            self.lista_materiales.clear()
            
            materiales = obtener_materia_prima()
            
            if materiales:
                for material in materiales:
                    texto_item = f"{material['nombre']} - ${material['precio_por_gramo']}/g ({material['tipo']})"
                    item = QListWidgetItem(texto_item)                
                    item.setData(Qt.UserRole, material['id'])
                    self.lista_materiales.addItem(item)
            else:
                self.lista_materiales.addItem("No hay materiales registrados")
                
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudieron cargar los materiales: {str(e)}")


    def agregar_material(self):
        nombre, ok = QInputDialog.getText(self, "Agregar Material", "Nombre del material:")
        if not ok or not nombre.strip():
            return

        precio, ok = QInputDialog.getDouble(
            self, "Precio", "Precio por gramo:",
            decimals=2
        )
        if not ok:
            return

        tipos = ["cera", "aditivo", "escencia", "alcohol", "yeso", "agua"]
        tipo, ok = QInputDialog.getItem(
            self, "Tipo", "Selecciona el tipo:",
            tipos, current=0, editable=False
        )
        if not ok:
            return

        try:
            resultado = agregar_materia_prima(nombre.strip(), precio, tipo)       
            if resultado is not None:
                QMessageBox.information(self, "Éxito", "Material agregado correctamente")
                self.cargar_materiales() 
            else:
                QMessageBox.critical(self, "Error", "No se pudo agregar el material")            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al agregar material: {str(e)}")


    def editar_material(self):
        item_seleccionado = self.lista_materiales.currentItem()
        if not item_seleccionado:
            QMessageBox.warning(self, "Advertencia", "Selecciona un material para editar")
            return

        material_id = item_seleccionado.data(Qt.UserRole)
        material = obtener_materia_prima_id(material_id)
        if not material:
            QMessageBox.critical(self, "Error", "No se encontró el material seleccionado")
            return
        material = material[0]

        nombre, ok = QInputDialog.getText(
            self, "Editar Material", "Nombre del material:",
            text=material['nombre']
        )
        if not ok or not nombre.strip():
            return

        precio, ok = QInputDialog.getDouble(
            self, "Precio", "Precio por gramo:",
            value=material['precio_por_gramo'], decimals=2
        )
        if not ok:
            return

        tipos = ["cera", "aditivo", "escencia", "alcohol", "yeso", "agua"]
        tipo, ok = QInputDialog.getItem(
            self, "Tipo", "Selecciona el tipo:",
            tipos, current=tipos.index(material['tipo']), editable=False
        )
        if not ok:
            return

        try:
            resultado = actualizar_materia_prima(material_id, nombre.strip(), precio, tipo)
            if resultado is not None:
                QMessageBox.information(self, "Éxito", "Material actualizado correctamente")
                self.cargar_materiales()
            else:
                QMessageBox.critical(self, "Error", "No se pudo actualizar el material")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al actualizar material: {str(e)}")


    def eliminar_material(self):
        item_seleccionado = self.lista_materiales.currentItem()
        if not item_seleccionado:
            QMessageBox.warning(self, "Advertencia", "Selecciona un material para eliminar")
            return

        material_id = item_seleccionado.data(Qt.UserRole)

        if verificar_material_en_uso(material_id):
            QMessageBox.warning(
                self, "No se puede eliminar",
                "Este material está siendo usado en una o más recetas.\n"
                "Elimínalo de las recetas primero."
            )
            return

        confirmacion = QMessageBox.question(
            self, "Confirmar Eliminación",
            "¿Estás seguro de que deseas eliminar este material?",
            QMessageBox.Yes | QMessageBox.No
        )
        if confirmacion != QMessageBox.Yes:
            return

        try:
            resultado = eliminar_materia_prima(material_id)
            if resultado is not None:
                QMessageBox.information(self, "Éxito", "Material eliminado correctamente")
                self.cargar_materiales()
            else:
                QMessageBox.critical(self, "Error", "No se pudo eliminar el material")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al eliminar material: {str(e)}")