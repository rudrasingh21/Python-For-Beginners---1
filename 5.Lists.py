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