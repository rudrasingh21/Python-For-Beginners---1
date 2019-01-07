----------
Generators:-
----------

Yield and Return:-

Return:- Function basically return value , and destroys all local variable and State.

Yield:- returns the value but It preservs its previous one.

>>> def remote_control_next():
...     yield "CNN"
...     yield "ESPN"
...
>>> a = remote_control_next()

>>> a
<generator object remote_control_next at 0x000001D665B539E8>

>>> next(a)
'CNN'
>>> next(a)
'ESPN'

>>> for i in remote_control_next():
...     print(i)
...
CNN
ESPN

-----------------
Fibonacci Program:-
-----------------

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

for f in fib():
    if f > 100:
        break
    print(f)