class Comida():
    def __init__(self):
        self.tipoComida = None
        self.tamaño = None
        self.sabor = None
        self.nombre = None
        self.valor = None

    def precio(self):
        return self.valor

def main():
    plato1 = Comida()
    plato1.tipoComida = "Chino"
    plato1.tamaño = "Familiar"
    plato1.sabor = "Salado y picante"
    plato1.nombre = "SHAOFAN"
    plato1.valor = '50k'

    plato2 =Comida()
    plato2.tipoComida = "Colombiana"
    plato2.tamaño = "Corrientazo"
    plato2.sabor = "Salado y dulce"
    plato2.nombre = "Peto Dulce"
    plato2.valor = '12k'

    print(f'\nBienvendido al restaurante ¡SIRVALO PUES!\n'
          f'1. {plato1.nombre}, un tipo de plato {plato1.tipoComida}'
          f' El tamaño del plato es {plato1.tamaño} que tiene sabor'
          f' {plato1.sabor}\n'
          f'Precio: {plato1.precio}\n')
    
    print(f'2. {plato2.nombre}, un tipo de plato {plato2.tipoComida}'
          f' El tamaño del plato es {plato2.tamaño} que tiene sabor'
          f' {plato2.sabor}\n'
          f'Precio: {plato2.precio()}\n')


if __name__ == "__main__":
    main()