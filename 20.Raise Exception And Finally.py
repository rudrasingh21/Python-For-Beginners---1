'''try:
    raise MemoryError('memory error')
except MemoryError as e:
    print(e)

# MemoryError :- is built in exception
# Exception   :- is a class
try:
    raise Exception('memory error')
except Exception as e:
    print(e)'''

# To define User define Exception you need to define a class:-

class Accident(Exception):   #Accident is derive from Exception class
    def __init__(self,msg):
        self.message = msg

    def print_exception(self):
        print("User defined exception: ",self.message)
#Above we have defined User defined exception class

#Now raise it 

try:
    raise Accident('crash between two cars')
except Accident as e:
    e.print_exception()

#OUTPUT:- User defined exception:  crash between two cars

#Let's Handle Exception:-

'''class Accident(Exception):   #Accident is derive from Exception class
    def __init__(self,msg):
        self.message = msg

    def handle(self):
        print("Accident occured, take detour")
#Above we have defined User defined exception class

try:
    raise Accident('crash between two cars')
except Accident as e:
    e.handle()
    
OUTPUT:- Accident occured, take detour'''