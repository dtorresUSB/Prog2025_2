from random import randint as r

def listado():      #crear una lista de numeros aleatorios sin repetir
    n = int(input('Cuantos numeros quiere generar: '))
    datos=0         #indica el numero de elementos dentro de la lista
    lista=[]
    while datos<n:
        numero = r(0,100)
        if numero not in lista:
            lista.append(numero)
            datos+=1
    return lista

def faltantes(lista):
    minimo = min(lista)
    maximo = max(lista)
    enLista=[]
    perdidos=[]
    for i in range(minimo,maximo+1):
        if i in lista:
            enLista.append(i)
        else:
            perdidos.append(i)

    print(enLista)
    print(perdidos)

def main():
    lista = listado()
    faltantes(lista)



if __name__ == "__main__":
    main()