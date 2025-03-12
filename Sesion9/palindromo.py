
def quitarEspacios(texto):
    txt = ''
    for i in texto:
        if i != ' ':
            txt+=i
    return txt

def reves(texto):
    txt = ''
    for i in range(-1,-len(texto)-1,-1):    #(inicio,fin,paso)
        txt+=texto[i]
    return txt

def main():
    texto = input('Ingrese una frase\n').lower()
    texto = quitarEspacios(texto)
    texto2 = reves(texto)
    if texto == texto2:
        print('Si es palindromo')
    else:
        print('No es palindromo')


if __name__ == "__main__":
    main()