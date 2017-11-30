# -*- coding: utf-8 -*-
from numpy import sin, arange

a = 1.48
b = 3.51

funa = sin(a)
funb = sin(b)

if funa * funb  > 0:
    print "Intervālā [%.2f,%.2f] sākņu nav vai ..."%(a,b)
    exit

delta_x = 0.01
k = 0
while (b - a) > delta_x:
    x = (a+b)/2.
    funx = sin(x)
    if funa * funx > 0:
        a = x
    else:
        b = x
    k = k + 1
print "tika dalīts %d reizes, x = %.5f a = %.5f b = %.5f"%(k,x,a,b)
print b-a
