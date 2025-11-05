from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton, QFormLayout, QGroupBox)
from PyQt5.QtCore import Qt
from database.consultas import (
    obtener_receta_por_tipo,
    obtener_envase_por_tipo,
    obtener_costo_fijo_tipo,
    obtener_ingredientes_receta,
    obtener_envase_por_id
)

class CalcuVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("SeccionPrincipal")
        self.init_ui()
        
    def init_ui(self):
        layout_principal = QVBoxLayout()
        layout_principal.setAlignment(Qt.AlignTop)
        
        titulo = QLabel("Calculadora de Costos")
        titulo.setObjectName("tituloPrincipal")
        layout_principal.addWidget(titulo)
        
        grupo_seleccion = QGroupBox("Seleccionar Producto")
        layout_seleccion = QFormLayout()
        
        self.combo_producto = QComboBox()
        self.combo_producto.addItem("Vela", "vela")
        self.combo_producto.addItem("Refill Vela", "refill") 
        self.combo_producto.addItem("Difusor", "difusor")
        self.combo_producto.addItem("Yeso", "yeso")
        self.combo_producto.currentIndexChanged.connect(self.actualizar_formulario)
        
        layout_seleccion.addRow("Tipo de producto:", self.combo_producto)

        self.combo_envase = QComboBox()
        layout_seleccion.addRow("Envase:", self.combo_envase)
        
        grupo_seleccion.setLayout(layout_seleccion)
        layout_principal.addWidget(grupo_seleccion)
        
        # Formulario de datos
        grupo_formulario = QGroupBox("Datos del Producto")
        layout_formulario = QFormLayout()
        
        self.input_peso_agua = QLineEdit()
        self.input_peso_agua.setPlaceholderText("Ej: 200")
        layout_formulario.addRow("Peso de agua (g):", self.input_peso_agua)
        
        self.input_margen = QLineEdit()
        self.input_margen.setPlaceholderText("Ej: 50")
        layout_formulario.addRow("Margen ganancia (%):", self.input_margen)
        
        grupo_formulario.setLayout(layout_formulario)
        layout_principal.addWidget(grupo_formulario)

        #Costos fijos
        self.grupo_costos_fijos = QGroupBox("Costos Fijos Aplicados")
        self.layout_costos_fijos = QVBoxLayout()
        self.grupo_costos_fijos.setLayout(self.layout_costos_fijos)
        layout_principal.addWidget(self.grupo_costos_fijos)
        
        self.btn_calcular = QPushButton("Calcular Costos")
        self.btn_calcular.clicked.connect(self.calcular_costos)
        layout_principal.addWidget(self.btn_calcular)
        
        self.label_resultados = QLabel("Los resultados son:")
        self.label_resultados.setWordWrap(True)
        layout_principal.addWidget(self.label_resultados)
        
        self.setLayout(layout_principal)

        self.actualizar_formulario()  # Cargar datos iniciales
        
    def actualizar_formulario(self):
        """Funcion para actualizar el formulario según el producto seleccionado"""
        producto = self.combo_producto.currentData()
        self.combo_envase.clear()
        envases = obtener_envase_por_tipo(producto)
        for envase in envases:
            self.combo_envase.addItem(f"{envase['nombre']} ($ {envase['precio']})", envase['id'])
        
        self.actualizar_costos_fijos(producto)
    
    def actualizar_costos_fijos(self, producto):
        """Mostrar costos fijos aplicados al producto en cuestion"""
        while self.layout_costos_fijos.count():
            child = self.layout_costos_fijos.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
            
        costos_fijos = obtener_costo_fijo_tipo(producto)
        if costos_fijos:
            for costo in costos_fijos:
                label = QLabel(f"{costo['concepto']}: $ {costo['precio']}")
                self.layout_costos_fijos.addWidget(label)
        else:
            label = QLabel("No hay costos fijos aplicados a este producto.")
            self.layout_costos_fijos.addWidget(label)

    def calcular_costos(self):
        producto = self.combo_producto.currentData()
        peso_agua = float(self.input_peso_agua.text())
        margen_ganancia = float(self.input_margen.text())
        margen_ganancia /= 100.0  # Convertir a decimal
        envase_id = self.combo_envase.currentData()
        receta = obtener_receta_por_tipo(producto)
        if not receta:
            self.label_resultados.setText("No se encontró una receta.")
            return
        receta = receta[0]
        densidad = float(receta['densidad'])
        peso_real = peso_agua * densidad

        ingredientes = obtener_ingredientes_receta(receta['id'])
        costo_materiales = 0.0
        detalle_ingredientes = []

        for ingrediente in ingredientes:
            gramos_ingrediente = peso_real * (float(ingrediente['porcentaje']) / 100.0)
            costo_ingrediente = gramos_ingrediente * float(ingrediente['precio_por_gramo'])
            costo_materiales += costo_ingrediente
            detalle_ingredientes.append(
                f"{ingrediente['nombre']}: {gramos_ingrediente:.1f} g x $ {ingrediente['precio_por_gramo']} /g = $ {costo_ingrediente:.2f}"
            )

        costo_envase = 0.0
        detalle_envase = " - Envase REFILL $0.00"

        if producto != "refill" and envase_id:
            envase_data = obtener_envase_por_id(envase_id)
            if envase_data:
                envase = envase_data[0]
                costo_envase = float(envase['precio'])
                detalle_envase = f" - Envase {envase['nombre']} $ {costo_envase:.2f}"

        costos_fijos = obtener_costo_fijo_tipo(producto)
        costo_fijos_total = sum(float(costo['precio']) for costo in costos_fijos)
        detalle_fijos = [f" {costo['concepto']}: $ {costo['precio']}" for costo in costos_fijos]

        costo_total = costo_materiales + costo_envase + costo_fijos_total
        precio_venta = costo_total * (1 + margen_ganancia)

        self.mostrar_resultados(
            peso_agua=peso_agua, peso_real=peso_real, densidad=densidad,
            costo_materiales=costo_materiales, detalle_ingredientes=detalle_ingredientes,
            costo_envase=costo_envase, detalle_envase=detalle_envase,
            costo_fijos_total=costo_fijos_total, detalle_fijos=detalle_fijos,
            costo_total=costo_total, margen_ganancia=margen_ganancia, precio_venta=precio_venta
        )

    def mostrar_resultados(self, peso_agua, peso_real, densidad,
                          costo_materiales, detalle_ingredientes,
                          costo_envase, detalle_envase,
                          costo_fijos_total, detalle_fijos,
                          costo_total, margen_ganancia, precio_venta):
        resultados = f"""
        RESULTADOS DE CÁLCULO: <br>
        - Peso de agua: {peso_agua:.1f} g <br>
        - Peso real del producto: {peso_real:.1f} g -  (Densidad: {densidad})<br><br>
        - Costo de materiales: $ {costo_materiales:.2f}<br>
            {"<br>".join([f"- {ing}" for ing in detalle_ingredientes])}<br><br>
        - Costo de envase: $ {costo_envase:.2f}{detalle_envase}<br><br>
        - Costo de costos fijos: $ {costo_fijos_total:.2f}<br>
            {"<br>".join([f"- {costo}" for costo in detalle_fijos])}<br><br>
        RESUMEN:<br>
        - Costo total del producto: $ {costo_total:.2f}<br>
        - Margen de ganancia: {margen_ganancia:.1f} %<br>
        - Precio de venta sugerido: $ {precio_venta:.2f}<br>
        """
        self.label_resultados.setText(resultados)