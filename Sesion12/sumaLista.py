from random import randint as r


def aleatorio(n):
    lista = []
    for i in range(n):
        lista.append(r(0,10))
    return lista

def sumaDatos(lista):
    if len(lista)>1:
        numero=lista.pop(0)
        resultado = numero + sumaDatos(lista)
    else:
        return lista[0]
        #resultado = lista[0]
    return resultado


if __name__ == "__main__":
    n = int(input('Cuantos numeros quiere dentro de la lista: '))
    datos = aleatorio(n)
    print(datos)
    print(sumaDatos(datos))