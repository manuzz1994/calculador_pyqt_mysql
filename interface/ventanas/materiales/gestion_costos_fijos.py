from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton, QHBoxLayout, QListWidgetItem, QInputDialog, QMessageBox
from PyQt5.QtCore import Qt
from database.consultas import obtener_costos_fijos, obtener_costo_fijo_tipo, agregar_costo_fijo, editar_costo_fijo, eliminar_costo_fijo

class GestionCostosFijos(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.cargar_costos_fijos()

    def init_ui(self):
        layout = QVBoxLayout()
        titulo = QLabel("Gestión de Costos Fijos")
        layout.addWidget(titulo)

        self.lista_costos = QListWidget()
        layout.addWidget(self.lista_costos)

        layout_btn = QHBoxLayout()
        self.btn_agregar = QPushButton("Agregar Costo Fijo")
        self.btn_editar = QPushButton("Editar Costo Fijo")
        self.btn_eliminar = QPushButton("Eliminar Costo Fijo")
        self.btn_actualizar = QPushButton("Actualizar Lista")

        self.btn_agregar.clicked.connect(self.agregar_costo_fijo)
        self.btn_editar.clicked.connect(self.editar_costo_fijo)
        self.btn_eliminar.clicked.connect(self.eliminar_costo_fijo)
        self.btn_actualizar.clicked.connect(self.cargar_costos_fijos)

        layout_btn.addWidget(self.btn_agregar)
        layout_btn.addWidget(self.btn_editar)
        layout_btn.addWidget(self.btn_eliminar)
        layout_btn.addWidget(self.btn_actualizar)
        layout.addLayout(layout_btn)
        self.setLayout(layout)

    def cargar_costos_fijos(self):
        self.lista_costos.clear()
        costos = obtener_costos_fijos()
        for costo in costos:
            item_text = f"{costo['id']}: {costo['concepto']} - ${costo['precio']} (Aplica a: {costo['aplica_a']})"
            item = QListWidgetItem(item_text)
            item.setData(Qt.UserRole, costo['id'])  # Guardar el diccionario completo en el item
            self.lista_costos.addItem(item)

    def agregar_costo_fijo(self):
        concepto, ok1 = QInputDialog.getText(self, "Agregar Costo Fijo", "Concepto:")
        if not ok1 or not concepto:
            return
        precio, ok2 = QInputDialog.getDouble(self, "Agregar Costo Fijo", "Precio:", decimals=2)
        if not ok2:
            return
        
        aplica_a = ['todos', 'vela_refill', 'difusor', 'yeso']
        aplica_a, ok3 = QInputDialog.getItem(self, "Agregar Costo Fijo", "Aplica a:", ["todos", "vela_refill", "difusor", "yeso"], 0, False)
        if not ok3:
            return

        resultado = agregar_costo_fijo(concepto, precio, aplica_a)
        if resultado is not None:
            QMessageBox.information(self, "Éxito", "Costo fijo agregado correctamente.")
            self.cargar_costos_fijos()
        else:
            QMessageBox.warning(self, "Error", "No se pudo agregar el costo fijo.")

    def editar_costo_fijo(self):
        costo_seleccionado = self.lista_costos.currentItem()
        if not costo_seleccionado:
            QMessageBox.warning(self, "Error", "Seleccione un costo fijo para editar.")
            return
        
        costo_id = costo_seleccionado.data(Qt.UserRole)
        concepto, ok1 = QInputDialog.getText(self, "Editar Costo Fijo", "Nuevo Concepto:")
        if not ok1 or not concepto:
            return
        precio, ok2 = QInputDialog.getDouble(self, "Editar Costo Fijo", "Nuevo Precio:", decimals=2)
        if not ok2:
            return
        
        aplica_a = ['todos', 'vela_refill', 'difusor', 'yeso']
        aplica_a, ok3 = QInputDialog.getItem(self, "Editar Costo Fijo", "Nuevo Aplica a:", ["todos", "vela_refill", "difusor", "yeso"], 0, False)
        if not ok3:
            return

        resultado = editar_costo_fijo(costo_id, concepto, precio, aplica_a)
        if resultado is not None:
            QMessageBox.information(self, "Éxito", "Costo fijo editado correctamente.")
            self.cargar_costos_fijos()
        else:
            QMessageBox.warning(self, "Error", "No se pudo editar el costo fijo.")

    def eliminar_costo_fijo(self):
        costo_seleccionado = self.lista_costos.currentItem()
        if not costo_seleccionado:
            QMessageBox.warning(self, "Error", "Seleccione un costo fijo para eliminar.")
            return
        
        costo_id = costo_seleccionado.data(Qt.UserRole)

        confirmacion = QMessageBox.question(self, "Confirmar Eliminación", "¿Está seguro de eliminar este costo fijo?", QMessageBox.Yes | QMessageBox.No)
        if confirmacion == QMessageBox.Yes:
            resultado = eliminar_costo_fijo(costo_id)
            if resultado is not None:
                QMessageBox.information(self, "Éxito", "Costo fijo eliminado correctamente.")
                self.cargar_costos_fijos()
            else:
                QMessageBox.warning(self, "Error", "No se pudo eliminar el costo fijo.")