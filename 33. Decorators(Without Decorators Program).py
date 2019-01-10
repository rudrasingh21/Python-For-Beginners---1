# Without Decorators Code

import time

def calc_square(n):
    start = time.time()
    result = []
    for i in n:
        result.append(n*n)
    end = time.time()

    print("calc_square took " + str((end-start)*1000) + " mil sec")
    return result

def calc_cube(n):
    start = time.time()
    result = []
    for i in n:
        result.append(n*n*n)
    end = time.time()
    print("calc_cube took " + str((end-start)*1000) + "mil sec")
    return result

array = range(1000)

out_square = calc_square(array)

out_cube = calc_cube(array)


#NOTE:- The problem with this code is:-

#1) Code Duplication

#2) Less readability
