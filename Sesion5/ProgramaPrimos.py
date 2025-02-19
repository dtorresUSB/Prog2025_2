num = int(input('Ingrese un numero: '))
for i in range(2,num+1):
    if num%i == 0:
        if num == i:
            print('Si es primo')
        else:
            print('No es primo')
            break
