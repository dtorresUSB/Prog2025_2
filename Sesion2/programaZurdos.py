porcentaje = int(input('Porcentaje de zurdos que'+ 
                       'desea dentro de la habitacion: '))
personas = 100//(100-porcentaje)
personasFuera = 99-(personas-1)
print(personas)
print(f'El numero de zurdos que deben salir de la sala es: {personasFuera}')