import math as m
a=int(input('imgresa el valor de a:'))
b=int(input('imgresa el valor de b:'))
c=int(input('imgresa el valor de c:'))
p2=(b**2)-(4*a*c)
raiz=b**2-4*a*c
if raiz>0:
    x1=(-b+m.sqrt(p2))/(2*a)
    x2=(-b-m.sqrt(p2))/(2*a)
    print('la solucion es =',x1,'y/o',x2)
else:
    print('la solución es imaginaria, ya q la raiz es:',p2)
