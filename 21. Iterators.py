
>>> a =  ["hey","bro","you","are","awesome"]
>>> for i in a:
...  print(i)
...
hey
bro
you
are
awesome

__iter__ :- is a built in method.

__next__ :- is a built in method.

>>> itr = iter(a)
>>> itr
<list_iterator object at 0x000002555A4B3F98>
>>> next(itr)
'hey'
>>> next(itr)
'bro'
>>> next(itr)
'you'
>>> next(itr)
'are'
>>> next(itr)
'awesome'
>>> next(itr)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration


-------------------------
reverse : built in method
-------------------------

>>> itrrrr = reversed(a)
>>> next(itrrrr)
'awesome'
>>> next(itrrrr)
'are'
>>> next(itrrrr)
'you'
>>> next(itrrrr)
'bro'
>>> next(itrrrr)
'hey'

