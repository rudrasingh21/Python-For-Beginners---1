#Sharing Data Between Processes Using Queue

# In Multiprocessing , multiple processers has there own address space

# They Don't share address space

# In previous example , we saw that , inside and outside process don't share values.

# when  Global Variable passes in a process address space then it creates it's own copy, because of multiprocessing.

#QUEUE class use for multiprocessing

import time
import multiprocessing

def calc_square(numbers, q):
    for n in numbers:
        q.put(n*n)      #Put Method of Queue

if __name__ == "__main__":
    arr = [2,3,4,5]
#NOTE:- using Queue
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=calc_square, args=(arr,q))   #passing q
#arr is a tuple so , is there.
#NOTE:- square_result Global Variable passes in p and creates it's own copy because of multiprocessing.

#to start multiprocessing we need to start it as below.
    p.start()

#We also need JOIN , so that after all multiprocessing printing (next step) will exec
    p.join()

    while q.empty() is False:
        print(q.get())