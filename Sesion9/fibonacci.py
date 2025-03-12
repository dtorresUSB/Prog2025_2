def serie1():
    a=0; b=1
    print(f'{a}\n{b}')
    for i in range (30):
        c = a
        a = b
        b = a + c
        print(b)

def serie2():
    a=0;b=1
    print(a)
    for i in range(30):
        print(b)
        a,b = b, a+b

def main():
    opc = input('Que opcion desea ejecutar: ')
    if opc == '1':
        serie1()
    elif opc == '2':
        serie2()    


if __name__ == "__main__":
    main()