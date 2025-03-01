from random import randint as r

def matriz(filas, columnas):
    array = []
    for i in range(filas):
        array.append([])            #Creando las filas
        for j in range(columnas):
            array[i].append(r(0,100))       #Creando las columnas
    print(array)
    return array

def impresion(datos):
    for i in datos:
        print(i)

def escalar(matriz):
    numero = int(input('Ingrese un escalar para la matriz: '))
    filas = len(matriz)
    columnas = len(matriz[0])
    for i in range(filas):
        for j in range(columnas):
            matriz[i][j] = numero*matriz[i][j]
    return matriz

def main():
    filas = int(input('Ingrese el numero de filas: '))
    columnas = int(input('Ingrese el numero de columnas: '))
    datos=matriz(filas, columnas)
    impresion(datos)
    datos = escalar(datos)
    impresion(datos)

if __name__=="__main__":
    main()