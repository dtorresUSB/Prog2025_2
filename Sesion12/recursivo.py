
def recursivoP(x):
    if x>0:
        recursivoP(x-1)
        print(x)
    print(f'Finalizó iteracion {x}')

if __name__ == "__main__":
    recursivoP(5)