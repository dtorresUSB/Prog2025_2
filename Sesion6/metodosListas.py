
def agregar(miLista):
    valor = int(input('Que numero desea agregar a la lista: '))
    miLista.append(valor)
    return miLista

def insertar(miLista):
    valor = int(input('Que valor desea ingresa: '))
    idx = int(input('¿En que posicion?: '))
    miLista.insert(idx,valor)
    return miLista

def borrar(miLista):
    miLista.clear()
    return miLista

def remover(miLista):
    valor = int(input('Que valor desea remover: '))
    miLista.remove(valor)
    return miLista

def main():
    miLista = []
    opciones = ['s',agregar,insertar,borrar,remover]
    while 1: 
        print('Seleccione una de las siguientes opciones: \n'
            '1. Agregar un valor a la lista\n'
            '2. Insertar un valor a la lista en una posicion específica\n'
            '3. Borra toda la lista\n'
            '4. Remover un numero de la lista\n'
            '0. Salir del programa\n')
        
        opc = int(input('Seleccione una opcion: '))

        if opciones[opc]!='s':
            opciones[opc](miLista)
        else:
            break
        print(miLista)


if __name__ == "__main__":
    main()