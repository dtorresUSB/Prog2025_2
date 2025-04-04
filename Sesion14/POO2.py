from comida import Comida
def ingresarPlatos():
    print(f'------------ Plato n. {len(carta)+1} -------------')
    plato = Comida()
    labels=['tipo de comida','tamaño','sabor','nombre','precio']
    setters=[plato.setTipoComida,plato.setTamaño,plato.setSabor,
             plato.setNombre,plato.setValorPrecio]
    
    for i in range(5):
        txt = f'Ingrese el {labels[i]}:'
        label = input(txt)
        setters[i](label)
    print('\n')
    carta.append(plato)
    return plato

def imprimirNombres():
    n=0
    for platos in carta:
        n+=1
        print(f'{n}.{platos.getNombre()}')

def preguntaPlato():
    print('Desea cambiar la información de cual plato:  \n')
    imprimirNombres()

    opc1 = int(input('Seleccione uno de los anteriores platos: '))
    return opc1

def modificarInfo():
    opc1 = preguntaPlato()

    labels=['tipo de comida','tamaño','sabor','nombre','precio']
    objetoCarta = carta[opc1-1]
    setters=[objetoCarta.setTipoComida,objetoCarta.setTamaño,
             objetoCarta.setSabor,objetoCarta.setNombre,
             objetoCarta.setValorPrecio]
    
    for i in range(5):
        print(f'{i+1}. {labels[i]}')

    opc2 = int(input('Que información desea cambiar: '))
    info =input('Ingrese el cambio de informacion: ')

    setters[opc2-1](info)

def imprimirMenu():
    n=0
    for platos in carta:
        n+=1
        print(f'{n}. {platos.getNombre()}, un tipo de plato {platos.getTipoComida()}'
            f' El tamaño del plato es {platos.getTamaño()} que tiene sabor'
            f' {platos.getSabor()}\n'
            f'Precio: {platos.getValorPrecio()}\n')

def cobroFinal():
    opc1 = preguntaPlato()
    carta[opc1-1].getCobro()
    print('\n')

def menu():
    print('Bienvendio al restaurante "PIDALO PUES"\n'
          '1. Ingresar un plato dentro de la carta\n'
          '2. Modificar informacion de un plato de la carta\n'
          '3. Mostrar el menú completo\n'
          '4. Realizar cobro')
    
    fcn = ['s',ingresarPlatos,modificarInfo,imprimirMenu,cobroFinal]
    opc = int(input('Seleccione una opcion: '))
    
    plato=fcn[opc]()
    

def main():
    while 1:
        menu()   


carta = []
if __name__ == "__main__":
    main()

#variables =>    precio, sabor      tipoComida          tipo_comida
#Clases=>        Comida()           TiposDeComida()
#funciones=>     cobrar()           cobrarCuenta()      cobrar_cuenta()
#Campos =>       self.precio        self.precioComida   self.precio_comida
#Metodos =>      precio()           precioComida()