class Vehiculo():
    def __init__(self):
        self.marca = None
        self.modelo = None

    def setMarca(self,marca:str):
        self.marca = marca

    def setModelo(self,modelo:str):
        self.modelo = modelo

    def getMarca(self):
        return self.marca
    
    def getModelo(self):
        return self.modelo
    
    def arrancar(self):
        return 'rrrrrrrrrrrrrrm'

class Coche(Vehiculo):
    def __init__(self):
        super().__init__()
        self.airbags = None

    def setAirbags(self,airbags:str):
        self.airbags = airbags

    def getAirbags(self):
        return self.airbags
    
    def abrirMaletero(self):
        return 'Maletero abierto'
    
    def arrancar(self):
        return 'Haciendo Drift'

class Motocicleta(Vehiculo):
    def __init__(self):
        super().__init__()
        self.numeroCascos=None

    def setNumeroCascos(self, numeroCascos:int):
        self.numeroCascos = numeroCascos

    def getNumeroCascos(self):
        return self.numeroCascos

    def hacerCaballito(self):
        return 'Vamos en una rueda'
    
    def arrancar(self):
        return 'de 0 a 100 en 3 segundos'