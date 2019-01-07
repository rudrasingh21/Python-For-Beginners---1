import time

def calc_square(numbers):
    print("Calculate Square Numbers")
    for n in numbers:
        time.sleep(0.2)
        print("Square: ",n*n)

def calc_cube(numbers):
    print("Calculate Cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print("Cube: ",n*n*n)

arr = [2,3,4]

t = time.time() #To know how much time it will take to execute
calc_square(arr)
calc_cube(arr)

print("done in : ", time.time()-t)

#NOTE:- The time taken in executing this program can be redused by using Multithreading
