numbers = [1,2,3,4,5,6,7,8,9]
even=[]
for i in numbers:
    if i%2==0:
        even.append(i)

print(even)

#Using List Comprihension we can reduse number of lines in code

even=[i for i in numbers if i%2==0]

print(even)

#sqr of number:-

sqr_numbers = [i*i for i in numbers]

print(sqr_numbers)