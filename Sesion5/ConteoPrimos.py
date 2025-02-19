from FcnPrimos import primos

cantidad = int(input('Cuantos numeros primos desea conocer: '))

n = 0       #Contador de numeros primos
numero = 2  #numero a evaluar
txt = ''    #variable para concatenar

while n < cantidad:
    if primos(numero):
        txt += f'{numero}, '
        n += 1
    numero += 1

print(txt.rstrip(', ')+ ".")

