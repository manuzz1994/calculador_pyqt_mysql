from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QComboBox, 
                             QLineEdit, QPushButton, QFormLayout, QGroupBox)
from PyQt5.QtCore import Qt
import mysql.connector

class CalcuVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("SeccionPrincipal")
        print("✅ CalcuVentana inicializada")  # Debug
        
        self.init_ui()
        
    def init_ui(self):
        layout_principal = QVBoxLayout()
        layout_principal.setAlignment(Qt.AlignTop)
        
        # Título
        titulo = QLabel("Calculadora de Costos")
        titulo.setObjectName("tituloPrincipal")
        layout_principal.addWidget(titulo)
        print("✅ Título añadido")  # Debug
        
        # Grupo de selección de producto
        grupo_seleccion = QGroupBox("Seleccionar Producto")
        layout_seleccion = QFormLayout()
        
        # Selector de tipo de producto
        self.combo_producto = QComboBox()
        self.combo_producto.addItem("Vela", "vela")
        self.combo_producto.addItem("Refill Vela", "refill") 
        self.combo_producto.addItem("Difusor", "difusor")
        self.combo_producto.addItem("Yeso", "yeso")
        self.combo_producto.currentIndexChanged.connect(self.actualizar_formulario)
        print("✅ ComboBox creado")  # Debug
        
        layout_seleccion.addRow("Tipo de producto:", self.combo_producto)
        grupo_seleccion.setLayout(layout_seleccion)
        layout_principal.addWidget(grupo_seleccion)
        
        # Formulario básico (sin dinámico por ahora)
        grupo_formulario = QGroupBox("Datos del Producto")
        layout_formulario = QFormLayout()
        
        self.input_peso_agua = QLineEdit()
        self.input_peso_agua.setPlaceholderText("Ej: 200")
        layout_formulario.addRow("Peso de agua (g):", self.input_peso_agua)
        
        self.input_margen = QLineEdit()
        self.input_margen.setPlaceholderText("Ej: 30")
        layout_formulario.addRow("Margen ganancia (%):", self.input_margen)
        
        grupo_formulario.setLayout(layout_formulario)
        layout_principal.addWidget(grupo_formulario)
        
        # Botón de cálculo
        self.btn_calcular = QPushButton("Calcular Costos")
        self.btn_calcular.clicked.connect(self.calcular_costos)
        layout_principal.addWidget(self.btn_calcular)
        print("✅ Botón añadido")  # Debug
        
        # Área de resultados
        self.label_resultados = QLabel("Los resultados aparecerán aquí...")
        self.label_resultados.setWordWrap(True)
        layout_principal.addWidget(self.label_resultados)
        
        self.setLayout(layout_principal)
        print("✅ Layout establecido")  # Debug
        
    def actualizar_formulario(self):
        """Esta función se llamará cuando cambie el producto"""
        producto = self.combo_producto.currentData()
        print(f"🔄 Producto cambiado a: {producto}")
        
    def calcular_costos(self):
        """Calcular los costos - versión simple para probar"""
        print("🔄 Botón calcular presionado")  # Debug
        
        producto = self.combo_producto.currentData()
        peso_agua = self.input_peso_agua.text()
        margen = self.input_margen.text()
        
        resultado = f"""
        📊 CÁLCULO REALIZADO:
        
        Producto: {producto}
        Peso agua: {peso_agua}g
        Margen ganancia: {margen}%
        
        (Esta es una versión de prueba - Los cálculos reales se implementarán pronto)
        """
        
        self.label_resultados.setText(resultado)
        print("✅ Resultados mostrados")  # Debug