import time as t
import random
import matplotlib.pyplot as plt
from automat import *

# method creates random array with 318 cells wood and 5 cells fire
def ramdom_Array(i): 
    a = init_Arry("Aufgabe3")
    c = 0
    while True:
        random.seed(i)
        x = (random.randint(0, 20))
        y = (random.randint(0, 20))
        if a[x][y] == 2:
            c += 1
            a[x][y] = 1
            if c == 118:
                break
        i += 1
    d = 0
    while True:
        random.seed(i)
        x = (random.randint(0, 20))
        y = (random.randint(0, 20))
        if a[x][y] == 2:
            d += 1
            a[x][y] = 0
            if d == 5:
                break
        i += 1
    return a

# method counts arrays that were set all on fire
def all_fire(a):
    for l in a:
        for val in l:
            if val !=0:
                return False
    return True

#method solves Aufgabe 1.4
def aufgabe_3():
    print("aufgabe3")
    count=0
    for i in range(10000):
        print("Simulation: ", i)
        a=ramdom_Array(i)
        b = a.copy()
        za = zellulear_Automat()
        _, c = za.run(b, 21, False)
        if all_fire(c):
            count+=1
    print(f"{10000 - count} of 10000 simulations were not completly set on fire")

aufgabe_3()