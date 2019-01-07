----------
Iterators:-
----------

a= ["How","are","you","rudra"]

for i in a:
	print(i)
'''	
Output:-
How
are
you
rudra
'''
>>> itr = iter(a)

>>> itr
<list_iterator object at 0x000001D665E36080>

>>> next(itr)
'How'
>>> next(itr)
'are'
>>> next(itr)
'you'
>>> next(itr)
'rudra'

Internally this uses an internal function "iter"

This "iter" method is built in method.

So basically for loop has an Iter function .
It iterate values one by one using next.

#--------------------------
#Iterating through a LIST:-
#--------------------------

for element in [1,2,3]:
	print(element)
	
--------------------------
Iterating through a TOUPLE:-
--------------------------

for element in (1,2,3):
	print(element)
	
----------------------------------
Iterating through a Dictonary Keys:-
----------------------------------

for key in {'one':1, 'two':2}:
	print(key)
	
---------------------------------------
Iterating all the charactor in a string:-
---------------------------------------

for char in "123":
	print(char)
	
---------------------------------------
Iterating through every line in a file:-
---------------------------------------

for line in open("myfile.txt"):
	print(line, end=' ')


************Reversed Method************

>>> itr = reversed(a)

>>> next(itr)
'rudra'
>>> next(itr)
'you'
>>> next(itr)
'are'
>>> next(itr)
'How'
>>> next(itr)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

----------------------------------------------------------------
Implementing Remote Control Class , when you press Next button ,
it will give you next channel.
----------------------------------------------------------------

class RemoteControl():
	def __init__(self):
		self.channels = ["HBO","CNN","ESPN","STAR"]
		self.index = -1				--index variable , i.e. what channel you are on , -1 is your TV is off.
	
	def __itr__(self):
		return self
		
	def __next__(self):
		self.index += 1 
		if self.index == len(self.channels):
			raise StopIteration
		return self.channels[self.index]
		
r = RemoteControl()
itr = iter(r)
print(next(itr))
