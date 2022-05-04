
from automat import zellulear_Automat

# solves Aufgabe 1.2
def aufgabe_1():
    array=[[0,1,1],[1,1,2],[1,2,1]]
    size=3
    za=zellulear_Automat()
    za.run(array,size,True) 
aufgabe_1()



