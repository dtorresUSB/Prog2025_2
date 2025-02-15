valorIVA = 0.19
valorTotal = int(input('Ingrese el valor total: '))
valorBase = valorTotal/(1+valorIVA)
#print('El valor base del producto es: ', round(valorBase,2), ' pesos')
#print('El valor base del producto es: ' + str(round(valorBase,2)) + 'pesos')
print(f'El valor base del producto es: {valorBase:.2f} pesos')