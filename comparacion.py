#importar librerias
import matplotlib.pyplot as plt
import math
import numpy as np
#definicion de la funcion y del metodo de biseccion
def fun(x):
    return math.exp(-x)-x

def biseccion(xi,xf,vparo):
    iter=[]
    verpa=[]
    error=100
    i=0
    while error>=vparo:
        pm=(xi+xf)/2.0
        #print (pm)
        iter.append(i+1)
        error=abs((vv-pm)*100/vv)
        verpa.append(error)
        i=i+1
        #aplicacion del teorea de Bolzano y eleccion de subintervalo
        if (fun(xi)*fun(pm)<0):
            xf=pm
        else:
            xi=pm
    return pm,iter,verpa

def falsa(xi,xf,vparo):
    iter=[]
    verpa=[]
    error=100
    i=0
    while error>=vparo:
        pm=xi-(fun(xi)*(xf-xi))/(fun(xf)-fun(xi))
        #print (pm)
        iter.append(i+1)
        error=abs((vv-pm)*100/vv)
        verpa.append(error)
        i=i+1
        #aplicacion del teorea de Bolzano y eleccion de subintervalo
        if (fun(xi)*fun(pm)<0):
            xf=pm
        else:
            xi=pm
    return pm,iter,verpa
#valores contantes limite iniciao, limite final y numero de puntos de la grafica
a,b,p=0,1,100
#valor verdadero a considerar
vv=0.567143
#variables donde se guardara los errores del metodo
vparo=.005
#calculo del dominio y codominio e la funcion
x = np.linspace(a,b,p)
y = [fun(i) for i in x]
#presentación de resultaods
plt.figure(figsize=(9, 3))
plt.subplot(121)
plt.xlabel("iteración")
plt.ylabel("erpv")
plt.title('[-2,5]')
xo,exb,eyb=falsa(-2,5,vparo)
plt.semilogy(exb,eyb,'-o',label='Regla falsa')
xo,exb,eyb=biseccion(-2,5,vparo)
plt.semilogy(exb,eyb,'-o',label='Bisección')
plt.legend()
plt.subplot(122)
xo,exb,eyb=falsa(a,b,vparo)
plt.semilogy(exb,eyb,'-o',label='Regla falsa')
xo,exb,eyb=biseccion(a,b,vparo)
plt.title('[0,1]')
plt.semilogy(exb,eyb,'-o',label='Bisección')
plt.xlabel("iteración")
plt.ylabel("erpv")
plt.legend()

plt.suptitle('$f(x)=e^{-x}-x$')
plt.show()
