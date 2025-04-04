class Comida():
    def __init__(self):
        self.tipoComida = None
        self.tamaño = None
        self.sabor = None
        self.nombre = None
        self.valor = None

    def setTipoComida(self,tipo):
        self.tipoComida = tipo

    def getTipoComida(self):
        return self.tipoComida
    
    def setTamaño(self,tamaño):
        if tamaño.capitalize() in ['Personal','Familiar','Duo']:
            self.tamaño = tamaño
        else:
            print('El tamaño solo puede ser Personal, Familiar o Duo')

    def getTamaño(self):
        return self.tamaño
    
    def setSabor(self,sabor):
        self.sabor = sabor

    def getSabor(self):
        return self.sabor
    
    def setNombre(self,nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre
    
    def setValorPrecio(self,precio):
        if int(precio.rstrip('k'))>0:
            self.valor = precio
        else:
            print('El precio no puede ser menor a 0')

    def getValorPrecio(self):
        return self.valor
    
    def getCobro(self):
        print(f'El valor final de pago es: {self.getValorPrecio()}')