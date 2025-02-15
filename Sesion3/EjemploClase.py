limiteSuperior=10
limiteInferior=-10
num = int(input('Ingrese un numero: '))
if num<=limiteSuperior:
    if num>=limiteInferior:
        if num%2==0:
            print('Numero dentro del rango y par')
        else:
            print('Numero dentro del rango e impar')
    else:
        print('El numero es muy bajo')
else:
    print('El numero es muy alto')