# Multiprocessing --> Process1  , process2 ....

# Every Process has there own address space.

#To communicate to each other ,
# they user interprocess communication like-- 'FILE' , 'Message Memory','shared memory'

#Error on one process don't affect other .
'''
import time
import multiprocessing

def calc_square(numbers):
    for n in numbers:
        time.sleep(5)   #adding it to check m.p. in task manager of windows
        print("Square " +str(n*n))

def calc_cube(numbers):
    for n in numbers:
        time.sleep(5)   # as disc above and
        print("Cube " +str(n*n*n))

if __name__ == "__main__":
    arr = [2,3,4,5]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,)) #arr is a tuple so , is there.
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

#to start multiprocessing we need to start it as below.

    p1.start()
    p2.start()

#We also need JOIN , so that after all multiprocessing printing (next step) will exec

    p1.join()
    p2.join()

    print("Done")
'''
# We can also store the result in GLOBAL Variable

#NOTE: you can check below :- With in and not with in result store


import time
import multiprocessing

square_result=[]    #Global Variable

def calc_square(numbers):
    global square_result
    for n in numbers:
          print("Square " +str(n*n))
          square_result.append(n*n)
    print("With in a process: result " + str(square_result))  # 1.

if __name__ == "__main__":
    arr = [2,3,4,5]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,)) #arr is a tuple so , is there.
    #NOTE:- square_result Global Variable passes in p1 and creates it's own copy because of multiprocessing.

#to start multiprocessing we need to start it as below.
    p1.start()

#We also need JOIN , so that after all multiprocessing printing (next step) will exec
    p1.join()

    print("Out side process Result " + str(square_result))
    print("Done")

#NOTE:- As above , because of multiprocessing , Every process has own address space ,
# so Program variable are not shared between two processes .
# So we need to to add #1. for getting a output in result.
# And another result , which is outside will not give result.
