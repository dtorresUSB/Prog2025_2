import sys
import PyQt5.QtWidgets as PyQt
from PyQt5 import uic

class Principal(PyQt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):
        uic.loadUi('calculadora.ui',self)
        self.show()

        self.calcular.clicked.connect(self.operaciones)

    def operaciones(self):
        if self.suma.isChecked():
            a=int(self.editor_numero1.text())
            b=int(self.editor_numero2.text())
            c=a+b
        else:
            c=0
        self.imprimir(c)

    def imprimir(self,c):
        self.resultado.setText(str(c))
        
def main():
    app = PyQt.QApplication([])
    window = Principal()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()