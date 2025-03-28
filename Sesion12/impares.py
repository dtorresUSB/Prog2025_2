
def sumaImpares(x):
    if x>0:
        resultado=(2*x-1)+sumaImpares(x-1)
    else:
        resultado=0
    return resultado


if __name__ == "__main__":
    num = int(input('Cuantos numeros impares quiere sumar: '))
    print(sumaImpares(num))