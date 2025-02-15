numero = int(input('Ingrese un numero: '))

for i in range(2,numero+1):
    if numero%i == 0:
        if numero == i:
            print('El numero es primo')
        else:
            print('El numero no es primo')
            break