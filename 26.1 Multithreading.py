#Multithreading , basically all thread are for same processes.
#Every thread has a specific task and using there own code.
#All thread shares the same Address Space.

#IF we have a global variable defined in our program , they can be accessed by all threads.

#If there is a error / memory leak in a thread , then it will impact entire process.

import time
import threading        #Used for multithreading

def calc_square(numbers):
    print("calcuate square numbers")
    for n in numbers:
        time.sleep(0.2)
        print("Square: ",n*n)

def calc_cube(numbers):
    print("Calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print("Cube: ",n*n*n)

arr = [2,3,4,5]

t = time.time()

#Now create a thread

t1 = threading.Thread(target=calc_square, args=(arr,))

t2 = threading.Thread(target=calc_cube, args=(arr,))


#To start threading -- to execute programs in parallal
t1.start()
t2.start()

#JOIN will use , to wait untill one thread is done.

t1.join()
t2.join()

#JOIN means done with one thread and back to main thread.

print("Done in time: ", time.time()-t)

#Using Multithreading , we can reduse execution time of program