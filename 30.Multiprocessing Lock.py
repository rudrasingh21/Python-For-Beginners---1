#Multiprocessing Lock

#WhenEver 2 process or threads trying to access shared resorce like - Shared Memory , Filr , DB
#In this scenarios we use Lock .

import time
import multiprocessing

def deposit(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()  #Passing and Using Lock
        balance.value = balance.value + 1
        lock.release()  #Releasing Lock

def withdraw(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()  #Passing and Using Lock
        balance.value = balance.value - 1
        lock.release()  #Releasing Lock

if __name__ == '__main__':
    balance = multiprocessing.Value('i', 200)
    lock = multiprocessing.Lock()       #Creating Lock
    d = multiprocessing.Process(target=deposit, args=(balance,lock))
    w = multiprocessing.Process(target=withdraw, args=(balance,lock))
    d.start()
    w.start()
    d.join()
    w.join()
    print(balance.value)
