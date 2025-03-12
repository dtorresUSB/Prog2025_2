texto = 'amor'
anagrama = ['roma','mora','mor','omar','amor','moras','rosa']

def esAnagrama(texto,palabra):
    for i in texto:
        if texto == palabra:
            return False
        elif i not in palabra:
            return False
    return True

def cantidadLetras(texto,lista):
    longitud = len(texto)
    check = []
    for i in lista:
        if len(i)!=longitud:
            check.append(False)
        else:
            check.append(esAnagrama(texto,i))
    return check

def main():
    check=cantidadLetras(texto,anagrama)
    print(check)

if __name__ == "__main__":
    main()