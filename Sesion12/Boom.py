def recursivoP(x):
    if x>0:
        print(x)
        recursivoP(x-1)

if __name__ == "__main__":
    recursivoP(5)
    print('BOOOOOOOM!!!')