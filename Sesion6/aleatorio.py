#from random import randint as r
import random as r

for i in range(5):
    print(r.randint(10,20), end='     ')
    print(f'{r.uniform(0,1):.2f}', end='     ')
    print(r.choice('esternocleidomastoideo'))