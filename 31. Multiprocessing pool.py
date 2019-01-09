#Multiprocessing Pool (Map Reduce)

#Using Pool --> map --> reduce

#NOTE:-

# it may be possible taht in your CPU , only 1 core is processing your program

# If you are doing lot of Image processing and computation then one core will not be a good idea

# In these scenarios we think about parallalism by using all core of CPU.

# We use map (dividing your input) and Reduce(aggregating) your output.

from multiprocessing import Pool

def f(n):
    return n*n

if __name__ == "__main__":
    array = [1,2,3,4,5]
    #create an object of pool class
    p = Pool()
    # map will divide equal work b/w all available CORES in CPU
    result = p.map(f,array)      #passing function and Input
    p.close()
    p.join()
    print(result)



#NOTE:- comparision b/w Pool processing and Serial Processing

from multiprocessing import Pool
import time

def f(n):
    sum = 0
    for i in range(1000):
        sum += i*i
    return sum

if __name__ == "__main__":
    t1 = time.time()
    p = Pool()
    result = p.map(f,range(10000))
    p.close()
    p.join()

    print("Pool processing time: ",time.time()-t1)

    t2 = time.time()
    result = []
    for i in range(10000):
        result.append(f(i))

    print("Serial processing time: ", time.time() - t2)
