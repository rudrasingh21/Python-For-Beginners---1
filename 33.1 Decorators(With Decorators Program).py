import time

#Use cases Decorators:- We can do 1) Logging , 2) Timing

#define Wrapper function

#Wrapper function will take function as an argument

#NOTE:- Function are first class Object in python i.e.
#       you can pass function as an argument to a function like below,
#       and you can return function as a value from another function.

#       One function inside another function
def time_it(func):
    def wrapper(*args, **kwargs):   #*args--> Positional arg and **kwargs--> keyword arguments
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__ +" took " + str((end-start)*1000) + "mil sec")     #__name__ -> Will return name of function
        return result
    return wrapper      #returning wrapper function

#Decorate
@time_it
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result

#Decorate
@time_it
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result

array = range(1,100000)
out_square = calc_square(array)
out_cube = calc_cube(array)