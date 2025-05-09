import sys
import PyQt5.QtWidgets as PyQt
from PyQt5 import uic
import serial
import time
from PyQt5.QtCore import QTimer

class Principal(PyQt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.puerto()
        self.initGUI()

    def puerto(self):
        puerto = 'COM5'
        baudios = 9600
        try:
            self.ser = serial.Serial(puerto, baudios, timeout=1)
            time.sleep(2)  # Espera a que el puerto esté listo
        except serial.SerialException as e:
            print(f"No se pudo abrir el puerto: {e}")
            self.ser = None

    def initGUI(self):
        uic.loadUi('contador.ui',self)
        self.show()

        self.timer = QTimer()
        self.timer.timeout.connect(self.actualizar_contador)
        self.timer.start(100)

    def actualizar_contador(self):
        if self.ser and self.ser.in_waiting > 0:
            try:
                linea = self.ser.readline().decode('utf-8').strip()
                self.contador_segundos.setText(str(linea))
            except Exception as e:
                print(f"Error leyendo del puerto: {e}")
        
def main():
    app = PyQt.QApplication([])
    window = Principal()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()