import time as t
import matplotlib.pyplot as plt
from automat import *
from matplotlib import colors


# plots histogram
def histogramm_plot(x_list,y_list):
    plt.bar(x_list, y_list)
    plt.xticks(x_list)
    plt.yticks(y_list)
    plt.xlabel('Index')
    plt.ylabel('Schritte')
    plt.show()


# solves Aufgabe 1.3
def aufgabe_2():
    n=21
    y_list=[]
    x_list=[]
    s=0
    x=1
    for i in range (n):
        for j in range(n):
            print("Simulation: ",x)
            x+=1
            a=init_Arry("Aufgabe2")
            b = a.copy()
            b[i][j]=0
            za=zellulear_Automat()
            val,_=za.run(b,n,False)
            y_list.append(val)
            x_list.append(str(i*j))
            s+=val
    print("Average steps: ", s/441)
    histogramm_plot(x_list,y_list)
aufgabe_2()
