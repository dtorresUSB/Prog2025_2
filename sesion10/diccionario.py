estudiantes = {'nombres':['David','Pedro','Juan','Camilo'],
               'codigos':[5413215,5464535,4234545,548215]}
print(estudiantes['nombres'][0])

for i in range(len(estudiantes['nombres'])):
    print(f'El estudiante {estudiantes['nombres'][i]}',
          f'tiene codigo {estudiantes['codigos'][i]}')