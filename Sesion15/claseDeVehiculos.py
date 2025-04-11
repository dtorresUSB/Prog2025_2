import vehiculos

def tipoVehiculo(objeto):
    mtd=''
    if type(objeto) == vehiculos.Motocicleta:
        mtd = f'Numero de cascos: {objeto.getNumeroCascos()}\n' + \
            f'{objeto.hacerCaballito()}\n'
    elif type(objeto) == vehiculos.Coche:
        mtd = f'Numero de airbags: {objeto.getAirbags()}\n' + \
        f'{objeto.abrirMaletero()}\n'
    mtd += objeto.arrancar()
    return mtd

def estadoParking(parking):   
    i = 0
    for campos in parking:
        i+=1
        mtd = tipoVehiculo(campos)
        print(f'Estacionamiento {i}=> Marca: {campos.getMarca()}\n'
              f'                    Modelo: {campos.getModelo()}\n'
              f'                    {mtd}')   

def info(vehiculo, parking):
    vehiculo.setMarca(input('Indique la marca: '))
    vehiculo.setModelo(input('Indique el modelo: '))
    parking.append(vehiculo)

def garaje():
    parking = []
    while 1:
        print('Bienvenido al parqueadero de vehiculos "LOS 3 CHIFLADOS"\n'
            '1. Estacionar un coche\n'
            '2. Estacionar una motocicleta\n'
            '3. Estacionar una bicicleta\n'
            '4. Conocer el numero de vehiculos estacionados\n')
        
        opc = input('Seleccione una de las opciones: ')

        if opc == '1':
            vehiculo = vehiculos.Coche()
            vehiculo.setAirbags(input('Indique el # de airbags: '))
            info(vehiculo,parking)
        elif opc == '2':
            vehiculo = vehiculos.Motocicleta()
            vehiculo.setNumeroCascos(input('Ingrese el numero de cascos: '))
            info(vehiculo,parking)
        elif opc == '3':
            vehiculo = vehiculos.Vehiculo()
            info(vehiculo,parking)
        elif opc == '4':
            estadoParking(parking)

if __name__ == "__main__":
    garaje()