universidad={'mecatronica':{'nombres':['David','Pedro','Juan','Camilo'],
                            'codigos':[5413215,5464535,4234545,548215],
                            'genero':[1,1,1,1]},
             'sonido':{'nombres':['Edilberto', 'Johana', 'Maria','Alfredo','Kaila'],
                       'codigos':[8974654,5465453,3356851,456354,453238],
                       'genero':[1,0,0,1,0]}}

def impresion(diccionario,programa):
    for i in range(len(diccionario['nombres'])):
        if diccionario['genero'][i]==1:
            txt='El'
        else:
            txt='La'
        print(f'{txt} estudiante {diccionario['nombres'][i]}'
              f' tiene codigo {diccionario['codigos'][i]}'
              f' y pertenece al programa {programa}')

def listado(universidad):
    for i in universidad:
        impresion(universidad[i],i)

while 1:
    print('\nSeleccione una de las siguientes opciones: \n'
        '1. Listar los estudiantes de Mecatronica\n'
        '2. Listar los estudiantes de Sonido\n'
        '3. Listar a todos los estudiantes\n'
        '4. Salir')

    opc = input('Ingrese su seleccion: ')

    if opc == '1':
        impresion(universidad['mecatronica'],list(universidad.keys())[0])
    elif opc == '2':
        impresion(universidad['sonido'],list(universidad.keys())[1])
    elif opc == '3':
        listado(universidad)
    else:
        break
