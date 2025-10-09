from PyQt5.QtWidgets import QApplication
from interface.ventana_principal import VentanaPrincipal
import sys
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
        # --- Cargar archivo de estilos ---
    with open("estilos/estilos.qss", "r") as archivo_estilos:
        app.setStyleSheet(archivo_estilos.read())
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())