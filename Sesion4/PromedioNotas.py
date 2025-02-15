suma = 0
cantidadNotas = int(input('Ingrese la cantidad de notas: '))
for i in range(cantidadNotas):
    txt = f'Ingrese la nota #{i+1}: '
    nota = float(input(txt))
    suma += nota
notaFinal = suma/cantidadNotas
print(f'Su nota final es: {notaFinal:.1f}')