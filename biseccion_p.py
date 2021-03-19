#importar librerias
import matplotlib.pyplot as plt
import math
import numpy as np
#definicion de la funcion y del metodo de biseccion
def fun(x):
    return math.exp(-x)-x
def biseccion(xi,xf):
    return ((xi+xf)/2.0)
#valores contantes limite iniciao, limite final y numero de puntos de la grafica
a,b,p=-2,5,100
#valor verdadero a considerar
vv=0.567143
#variables donde se guardara los errores del metodo
exb=[]
eyb=[]
vpm=[]
#calculo del dominio y codominio e la funcion
x = np.linspace(a,b,p)
y = [fun(i) for i in x]
#variables auxiliares
error=100
i=0
while error>.005:
    #metodo de biseccion
    pm=biseccion(a,b)
    exb.append(i+1)
    vpm.append(pm)
    error=abs((vv-pm)*100/vv)
    eyb.append(abs((vv-pm)*100/vv))
    print (pm,abs((vv-pm)*100/vv))
    i=i+1
    #aplicacion del teorea de Bolzano y eleccion de subintervalo
    if (fun(a)*fun(pm)<0):
        b=pm
    else:
        a=pm
#presentación de resultaods
plt.figure(figsize=(9, 3))
plt.subplot(131)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x,y)
plt.subplot(132)
plt.xlabel("iteración")
plt.ylabel("Raíz")
plt.plot(exb,vpm,'-o')
plt.subplot(133)
plt.xlabel("iteración")
plt.ylabel("erpv")
plt.semilogy(exb,eyb,'-o')
plt.suptitle('Bisección')
plt.show()
