import time as t
import matplotlib.pyplot as plt
from matplotlib import colors


class  zellulear_Automat:

    def __init__(self,Array=[],n=10):
        self.Array=Array
        self.n=n

    # method creates woods
    def number_of_woods(self,za,a,x,y):   
        w=0                                                    
        for i in range(x-1,x+2):                              
            for j in range(y-1,y+2):                           
                if i < 0 or j < 0 or i >= za.n or j >=za.n:
                    continue
                else:
                    if a[i][j]==2:
                        w+=1
        return w

    # method creates fire
    def number_of_fire(self,za, a, x, y):
        f = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i < 0 or j < 0 or i >= za.n or j >= za.n:
                    continue
                else:
                    if a[i][j] == 0:
                        f += 1
        return f

    # rules for spreading fire and woods
    def rules(self,za,a):
        b=[]
        for i in range(za.n):
            l=[]
            for j in range(za.n):
                if a[i][j]==0:
                    l.append(0)
                elif a[i][j]==1:
                    if self.number_of_fire(za,a,i,j) >0:
                        l.append(0)
                    elif self.number_of_woods(za,a,i,j) > 1:
                        l.append(2)
                    else:
                        l.append(1)
                elif a[i][j]==2:
                    if self.number_of_fire(za,a,i,j) > 2:
                        l.append(0)
                    else:
                        l.append(2)
            b.append(l)
        return a,b
    
    # array output in terminal + graphic window
    @staticmethod
    def print_array(name,a):
        print(name)
        for l in a:
            for val in l:
                print(val,end=" ")
            print("")
        cmap = colors.ListedColormap(['red', 'lightgreen','green']) # Code for graphic layout start
        plt.ion()                                                   #
        plt.figure(figsize=(6,6))                                   #
        plt.pcolor(a[::-1],cmap=cmap,edgecolors='k', linewidths=3)  #
        plt.pause(0.5)                                              #
        plt.show()                                                  # end
        print("--------------------")
        
    @staticmethod
    def check(za,a,b):
        for i in range(za.n):
            for j in range(za.n):
                if a[i][j]!=b[i][j]:
                    return False
        return True
    
    # run zellulear automat    
    def run(self,a,n,show):
        za=zellulear_Automat(Array=a,n=n)
        count=0
        while True:
            a,b=self.rules(za,a)
            if show:
                self.print_array("a ",a)
            count+=1
            if za.check(za,a,b):
                break
            a=b.copy()
        return count,a


# inizialize Array for aufgabe 1.3/1.4    
def init_Arry(state):
    array=[]
    n=21
    if state=="Aufgabe2":
        for i in range(n):
            l=[]
            for j in range(n):
               if j<10:
                    l.append(1)
               else:
                    l.append(2)
            array.append(l)
    else:
        for i in range(n):
            l = []
            for j in range(n):
                l.append(2)
            array.append(l)
    return  array    
