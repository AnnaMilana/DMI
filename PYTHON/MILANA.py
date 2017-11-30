Python 2.7.3 (default, Mar 14 2014, 11:57:14) 
[GCC 4.7.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> print sinuss.__doc__

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    print sinuss.__doc__
NameError: name 'sinuss' is not defined
>>> from math import sin as sinuss
>>> print sinuss.__doc__
sin(x)

Return the sine of x (measured in radians).
>>> import math
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, 'sinuss': <built-in function sin>, '__name__': '__main__', '__package__': None, '__doc__': None, 'math': <module 'math' (built-in)>}
>>> math.cos
<built-in function cos>
>>> math.cos.__doc__
'cos(x)\n\nReturn the cosine of x (measured in radians).'
>>> math.cos(0.89)
0.6294120265736969
>>> import math as matemaatika
>>> vars()
{'matemaatika': <module 'math' (built-in)>, '__builtins__': <module '__builtin__' (built-in)>, 'sinuss': <built-in function sin>, '__name__': '__main__', '__package__': None, '__doc__': None, 'math': <module 'math' (built-in)>}
>>> acos(0.25)

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    acos(0.25)
NameError: name 'acos' is not defined
>>> from math import *
>>> print __builtins__.input.__doc__
input([prompt]) -> value

Equivalent to eval(raw_input(prompt)).
>>> 
