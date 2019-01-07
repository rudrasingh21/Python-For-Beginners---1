x=input("Enter Number1: ")
y=input("Enter Number2: ")
try:
    z = int(x) / int(y)
except Exception as e:
    print('Exception occered: ',e)
    z = None
print("Division is: ",z)

#NOTE:- Above is generic way of hadeling an exception
#We can give name to exception because it is known exception as below

x=input("Enter Number1: ")
y=input("Enter Number2: ")
try:
    z = int(x) / int(y)
except ZeroDivisionError as e:
    print('division by zero exception')
    z = None
print("Division is: ",z)

#*************************Other Example
#In below example we can see we defined x as STRING and Y as INTEGER
x=input("Enter Number1: ")
y=input("Enter Number2: ")
try:
    z = x / int(y)
except ZeroDivisionError as e:
    print('division by zero exception')
    z = None
except Exception as e:
    print("exception type: ",type(e).__name__)
    z = None
print("Division is: ",z)

#NOTE :- Using above code you will get name of exception ,
# Then as given below you can modify your program

x=input("Enter Number1: ")
y=input("Enter Number2: ")
try:
    z = x / int(y)
except ZeroDivisionError as e:
    print('division by zero exception')
    z = None
except TypeError as e:
    print("Type Error Exception")
    z = None
print("Division is: ",z)
