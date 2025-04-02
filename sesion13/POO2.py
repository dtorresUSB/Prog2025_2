class Comida():
    def __init__(self,tipo,tamaño,sabor,nombre,precio):
        self.tipoComida = tipo
        self.tamaño = tamaño
        self.sabor = sabor
        self.nombre = nombre
        self.valor = precio

    def precio(self):
        return self.valor

def main():
    menu = []

    for i in range(3):
        print(f'------------ Plato n. {i+1} -------------')
        tipo = input('Ingrese el tipo de plato: ')
        tamaño = input('Ingrese el tamaño del plato: ')
        sabor = input('Ingrese el sabor del plato: ')
        nombre= input('Cual es el nombre del plato: ')
        precio = input('Cual es el precio del plato: ')
        plato = Comida(tipo,tamaño,sabor,nombre,precio)
        menu.append(plato)
        print('\n')
    
    print(menu)

    n=0
    for platos in menu:
        n+=1
        print(f'{n}. {platos.nombre}, un tipo de plato {platos.tipoComida}'
            f' El tamaño del plato es {platos.tamaño} que tiene sabor'
            f' {platos.sabor}\n'
            f'Precio: {platos.precio()}\n')

if __name__ == "__main__":
    main()

#variables =>    precio, sabor      tipoComida          tipo_comida
#Clases=>        Comida()           TiposDeComida()
#funciones=>     cobrar()           cobrarCuenta()      cobrar_cuenta()
#Campos =>       self.precio        self.precioComida   self.precio_comida
#Metodos =>      precio()           precioComida()