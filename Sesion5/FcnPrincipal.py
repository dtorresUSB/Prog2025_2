from FcnPrimos import primos
# def imprimir():
#     print('Si es primo')

def main():
    print(__name__)
    num = int(input('Ingrese un numero: '))
    if primos(num):
        print('Si es primo')
    else:
        print('No es primo')

if __name__ == "__main__":
    main()