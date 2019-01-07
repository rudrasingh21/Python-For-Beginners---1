#SET is unordered collection of Unique records.
basket={"orange","apple","mango","apple","orange"}

print(type(basket))

print(basket)
#Output:
#{'mango', 'orange', 'apple'}
#you can see it gives you Unique record as output.

#OTHER Way

a=set()
a.add(1)
a.add(2)
a.add(3)

print(a)

b = {}

print(type(b))

#NOTE:- if you are giving blank {} , then it will be a directory

# if you are giving some value in {} , then it will be a SET.

#LIST allows Index operation , but SET don't allow Index operation.

#*******LIST to set**********

numbers=[1,2,3,4,1,2,3]

unique_number=set(numbers)

print(unique_number)

print(type(unique_number))

unique_number.add(5)

print(unique_number)

#*******FROZEN SET***************

fs=frozenset(numbers)

print(fs)

#NOTE:- Frozen set is same as Set , but it doesn't allow to add,
#So you can not change content of the set.




