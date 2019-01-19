item1 = "bread"
item2 = "Pasta"
item3 = "Fruits"

# All above are variable , We can create a List in this situation and access using Index

items = ["bread", "pasta", "fruits", "veggies"]

print(items)

print(items[0])
print(items[2])

# modify list =>change value of an element in a list

items[0] = "chips"
print(items)

# access elements from list from one location to another

print(items[0:2])
print(items[-1])

# We can append values using append

print(items)
items.append("butter")
print(items)

# Use Insert to insert data on a perticular place

items.insert(2, "EGG")
print(items)

# ADDING two lists

food = ["A", "B", "C"]
bathroom = ["x", "y", "z"]
print(food + bathroom)

#Find LENGTH

print(len(items))

#Find in List using :- in items

print ("A" in food)

print("x"  in food)

#List Operations 

>>> l=list(range(-6,7,2))
>>> l
[-6, -4, -2, 0, 2, 4, 6]

#List Operation

>>> [[x**2,x**3] for x in range(4)]
[[0, 0], [1, 1], [4, 8], [9, 27]]

--------------
# List clear() 
--------------

# Defining a list
l = [{1, 2}, ('a'), ['1.1', '2.2']]

# clearing the list
l.clear()

print('List:', l)

--------------
# List remove() 
--------------

list.remove(element)

# animal list
animal = ['cat', 'dog', 'rabbit', 'guinea pig']

# 'rabbit' element is removed
animal.remove('rabbit')

#Updated Animal List
print('Updated animal list: ', animal)

#output:- Updated animal list:  ['cat', 'dog', 'guinea pig']

--------------
# List delete() 
--------------

We can delete one or more items from a list using the keyword del. It can even delete the list entirely.

>>> my_list = ['p','r','o','b','l','e','m']
>>> del my_list[2]
>>> my_list
['p', 'r', 'b', 'l', 'e', 'm']
>>> my_list[2:5]
['b', 'l', 'e']
>>> my_list
['p', 'r', 'b', 'l', 'e', 'm']
>>> del my_list
>>> my_list
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'my_list' is not defined
