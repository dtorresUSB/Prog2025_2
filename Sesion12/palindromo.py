
def espacio(txt,indice=0):
    if indice!=len(txt): 
        if txt[indice] != ' ':
            print(txt[indice])
            concatenar = '' + txt[indice] + espacio(txt,indice+1)
        else:
            concatenar = '' + espacio(txt,indice+1)
    else:
        return ''
    print(concatenar)
    return concatenar

def palindromo():
    pass

if __name__ == "__main__":
    txt = "arriba la birra"
    espacio(txt)
    palindromo()