secreto = 6
numero = int(input('Ingrese un numero del 1 al 10: '))

while numero != secreto:        #Evalua la condicion verdadera
    print('JA JA no adivino!')
    numero = int(input('Ingrese un numero del 1 al 10: '))
print('Felicidades, casi no lo logra!')