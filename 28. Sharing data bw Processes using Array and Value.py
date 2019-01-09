
import multiprocessing

result = []

def calc_square(numbers):
    global result
    for n in numbers:
        result.append(n*n)
    print("Inside Process " + str(result))

if __name__ == "__main__":
    numbers = [2,3,4]
    p = multiprocessing.Process(target=calc_square,args=(numbers,))

    p.start()
    p.join()

    print("Outside Process " +str(result))

#NOTE:- Main process has result global variable
# and child process has calc_square process so it has it's own memory ,
# when we create a chile process , memory for global variable is copied. so seperate copy of result variable.


#**********Using SHARED Memory**************
#           2 ways of using SHARED Memory-->
#           (a)Using ARRAY
#           (b)Using VALUE

#===========> Creating Shared Memory Variable -> Using Array we can share data into two processes

import multiprocessing

def calc_square(numbers , result):   #Passing Shared memory which we created in __main__ , One more variable 'result'
    for idx , n in enumerate(numbers):   # i--> Index , n --> Value , to get index and value
        result[idx] = n*n
 
if __name__ == "__main__":
    numbers = [2,3,4]
    #Now Use Shared Memory Variable Array
    result = multiprocessing.Array('i',3)  #i-> int data type, 3--> size
    p = multiprocessing.Process(target=calc_square,args=(numbers,result))   #passing shared menory "result" in this process

    p.start()
    p.join()

    print(result[:])   # way to print all Elements in an Array

#===========> Creating Shared Memory Variable -> Using Value we can share data into two processes

import multiprocessing

def calc_square(numbers , result, v): #Passing Value to this process
    v.value = 5.67                      # setting value to process
    for idx , n in enumerate(numbers):   # to get index and value
        result[idx] = n*n


if __name__ == "__main__":
    numbers = [2,3,4]
    result = multiprocessing.Array('i',3)
    v = multiprocessing.Value('d',0.0)  #'d' --> double variable , assigned value 0.0
    p = multiprocessing.Process(target=calc_square,args=(numbers,result,v))   #passing shared menory "result" in this process

    p.start()
    p.join()

    print(v.value)   # way to print value
