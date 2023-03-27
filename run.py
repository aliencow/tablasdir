# print("Ingrese dos números para sumar.")
# input("numero uno")
# num1 = float(input("Ingrese el primer número: "))
# num2 = float(input("Ingrese el segundo número: "))
# resultado = num1 + num2
# print("El resultado de la suma es:", resultado)

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class Ventana(QWidget):

    def __init__(self):
        super().__init__()

        self.inicializar_ui()

    def inicializar_ui(self):
        

        # Crear widgets
        etiqueta_nombre = QLabel("Ingrese su nombre:")
        self.entrada_nombre = QLineEdit()
        boton_guardar = QPushButton("Guardar")

        # Conectar el botón a un manejador de eventos
        boton_guardar.clicked.connect(self.guardar_nombre)

        # Diseñar la ventana
        layout = QVBoxLayout()
        layout.addWidget(etiqueta_nombre)
        layout.addWidget(self.entrada_nombre)
        layout.addWidget(boton_guardar)

        self.setLayout(layout)
        self.setWindowTitle("Guardar Nombre")

    def guardar_nombre(self):
        nombre = self.entrada_nombre.text()

        # Guardar el nombre en un archivo
        with open("nombres.txt", "a") as archivo:
            archivo.write(nombre + "\n")

        # Limpiar la entrada
        self.entrada_nombre.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())
