
def lectura1():
    f = open('dataset//wcm.csv','rt',encoding='utf8')
    datos = f.readlines()
    DB = []
    for i in datos:
        DB.append(i.rstrip("\n").split(","))
    return DB
    
# def lectura2():
#     f = open('dataset//wcm.csv','rt',encoding='utf8')
#     datos = f.readlines()
#     DB = []
#     for i in range(len(datos)):
#         DB.append(datos[i].rstrip("\n").split(","))
#     print(DB)

# def lectura3():
#     f = open('dataset//wcm.csv','rt',encoding='utf8')
#     datos = f.readline().rstrip("\n").split(",")
#     DB = []
#     while datos != ['']:
#         DB.append(datos)
#         datos = f.readline().rstrip("\n").split(",")
#     print(DB)

def campeones(DB):
    lista_campeones = {}
    for partido in DB:
        if partido[12]=='Final':
            if partido[2]>partido[4] or partido[3]>partido[5]:
                campeon = partido[0]
            else:
                campeon = partido[1]
            if campeon not in lista_campeones:
                lista_campeones[campeon]=[partido[-1]]
            else:
                lista_campeones[campeon].append(partido[-1])
            print(f'La seleccion de {campeon} fue campeona en'
                        f'el año {partido[-1]}')
    
    for equipos in lista_campeones:
        print(f'{equipos} ha ganado {len(lista_campeones[equipos])}'
              ' copa mundo')

def main():
    datos = lectura1()
    print('Bienvenido al sistema estadistico de la FIFA World Cup\n'
          '1. Conocer los campeones de las copas mundo\n')
    opc = int(input('Cual su opcion seleccionada: '))
    menu = ['s',campeones]
    
    menu[opc](datos)


if __name__ == "__main__":
    main()