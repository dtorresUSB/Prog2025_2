def primos(numero):           #Unicamente ejecuta la tarea para la cual fue creada
    #print(__name__)
    for i in range(2,numero+1):
        if numero%i == 0:
            if numero == i:
                return True
            else:
                return False
            
if __name__ == "__main__":      #Prueba Unitaria
    print(primos(23))