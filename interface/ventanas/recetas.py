import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

"""
Aquí se implementará la gestión de recetas.
Aquí se definen las recetas, sus ingredientes y cantidades.
Tambien se agregará el costo fijo dependiendo de la receta.
Tendremos 4 recetas que estan conectadas a la calculadora.
IMPORTANTE:
Las recetas son siempre iguales para cada tipo de producto. Solo cambia la cantidad de ingredientes.

Velas: Cera Final 100%(Cera = 82% + Aditivo = 8% + Escencia = 10%) + envase de vela + costos fijos
Difusores: Liquido Final 100%(Alcohol = 75% + Escencia = 25%) + envase de difusor + costos fijos
Moldes yeso: Yeso Final 100%(Yeso = 90% + Agua = 10%) + costos fijos
Refill velas: Cera Final 100%(Cera = 82% + Escencia = 10% + Aditvo = 8%) + costos fijos SIN envase de vela
"""

# Ventana de Recetas
class Recetas(QWidget):
    pass