from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton, QHBoxLayout, QListWidgetItem, QMessageBox, QDialog, QDoubleSpinBox, QDialogButtonBox
from PyQt5.QtCore import Qt
from database.consultas import obtener_recetas, obtener_receta_por_id, obtener_ingredientes_receta, eliminar_ingrediente_receta, agregar_ingrediente_receta

class ListaRecetas(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()
        self.cargar_recetas()

    def init_ui(self):
        layout = QVBoxLayout()
        titulo = QLabel("Gestion de Recetas")
        titulo.setObjectName("tituloSeccion")
        layout.addWidget(titulo)

        self.lista_recetas = QListWidget()
        layout.addWidget(self.lista_recetas)

        layout_btn = QHBoxLayout()        
        btn_editar = QPushButton("Editar Porcentajes")
        btn_actualizar = QPushButton("Actualizar Lista")

        btn_actualizar.clicked.connect(self.cargar_recetas)
        btn_editar.clicked.connect(self.editar_receta)

        layout_btn.addWidget(btn_editar)
        layout_btn.addWidget(btn_actualizar)

        layout.addLayout(layout_btn)
        self.setLayout(layout)

    def cargar_recetas(self):
        try:
            self.lista_recetas.clear()
            recetas = obtener_recetas()

            for receta in recetas:
                # Obtener ingredientes de la receta
                ingredientes = obtener_ingredientes_receta(receta['id'])

                if ingredientes:
                    # Texto con ingredientes
                    ingredientes_text = " + ".join([
                        f"{ing['nombre']} ({ing['porcentaje']}%)" 
                        for ing in ingredientes])
                    item_text = f"{receta['nombre']} ({receta['tipo']}) - Ingredientes: {ingredientes_text}"
                else:
                    item_text = f"{receta['nombre']} ({receta['tipo']}) - Sin ingredientes"

                item = QListWidgetItem(item_text)
                item.setData(Qt.UserRole, receta['id'])
                self.lista_recetas.addItem(item)
        
        except Exception as e:
            print(f"Error al cargar recetas: {e}")

    def editar_receta(self):
        receta_id = self.obtener_receta_seleccionada()
        if not receta_id:
            QMessageBox.warning(self, "Error", "Seleccione una receta para editar.")
            return
        
        receta_data = obtener_receta_por_id(receta_id)
        ingredientes = obtener_ingredientes_receta(receta_id)
        if not receta_data:
            QMessageBox.warning(self, "Error", "No se pudo obtener la receta seleccionada.")
            return
        
        receta = receta_data[0]

        box_editor = QDialog(self)
        box_editor.setWindowTitle(f"Editar Receta: {receta['nombre']}")
        box_editor.setModal(True)
        box_editor.resize(350, 400)

        layout = QVBoxLayout()

        layout.addWidget(QLabel(f"Editando receta: {receta['nombre']}"))

        self.spinbox_porcentajes = {}
        for ingrediente in ingredientes:
            fila_layout = QHBoxLayout()
            label = QLabel(f"{ingrediente['nombre']}:")
            label.setMinimumWidth(150)
            fila_layout.addWidget(label)

            spinbox = QDoubleSpinBox()
            spinbox.setRange(0.1, 100.0)
            spinbox.setDecimals(1)
            spinbox.setSingleStep(0.1)
            spinbox.setValue(float(ingrediente['porcentaje']))
            spinbox.setSuffix(" %")
            spinbox.setMinimumWidth(100)

            fila_layout.addWidget(spinbox)
            fila_layout.addStretch()
            layout.addLayout(fila_layout)

            self.spinbox_porcentajes[ingrediente['id']] = spinbox
        
        self.label_total = QLabel("Total Porcentaje: 100.0%")
        layout.addWidget(self.label_total)

        buttons = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Cancel)
        buttons.accepted.connect(lambda: self.guardar_porcentajes(receta_id, ingredientes, box_editor))
        buttons.rejected.connect(box_editor.reject)
        layout.addWidget(buttons)

        for spinbox in self.spinbox_porcentajes.values():
            spinbox.valueChanged.connect(self.actualizar_total)
        
        self.actualizar_total()

        box_editor.setLayout(layout)
        box_editor.exec_()

    def actualizar_total(self):
        total = sum(spinbox.value() for spinbox in self.spinbox_porcentajes.values())
        color = "green" if 99.9 <= total <= 100.1 else "red"
        self.label_total.setText(f"Total Porcentaje: <span style='color:{color}'>{total:.1f}%</span>")

    def guardar_porcentajes(self, receta_id, ingredientes, dialog):
        try:
            total = sum(spinbox.value() for spinbox in self.spinbox_porcentajes.values())
            if not (99.9 <= total <= 100.1):
                QMessageBox.warning(self, "Error", f"El porcentaje total debe ser 100%.\nTotal actual: {total:.1f}%")
                return

            for ingrediente in ingredientes:
                spinbox = self.spinbox_porcentajes[ingrediente['id']]
                nuevo_porcentaje = spinbox.value()

                # Actualizar el ingrediente existente
                from database.consultas import actualizar_ingrediente_receta
                resultado = actualizar_ingrediente_receta(ingrediente['id'], nuevo_porcentaje)
                
                if resultado is None:
                    QMessageBox.critical(self, "Error", f"No se pudo actualizar {ingrediente['nombre']}")
                    return

            QMessageBox.information(self, "Éxito", "Porcentajes actualizados correctamente.")
            self.cargar_recetas()
            dialog.accept()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudieron guardar los cambios: {e}")
            
    def obtener_receta_seleccionada(self):
        item = self.lista_recetas.currentItem()
        return item.data(Qt.UserRole) if item else None        