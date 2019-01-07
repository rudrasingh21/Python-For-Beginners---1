*********************************
Exception And Finally Statement:-
*********************************

Exception in the Python are Instance of class.

try:
	raise Exception('Memory Error')
except Exception as e:
	print(e)
	
-------------

Using Exception we save our program to stop / terminate in middle and execute till end , 
We handle error which occure while execution of program.

x = input("Enter Number1: ")
y = input ("Enter Number2: ")
try:
    z = int(x)/int(y)
except Exception as e:
    print('exception occurd: ',e)
    z = None
print("Division is : ",z)

Output:-
Enter Number1: 16
Enter Number2: 0
exception occurd:  division by zero
Division is :  None

***************************

x = input("Enter Number1: ")
y = input ("Enter Number2: ")
try:
    z = int(x)/int(y)
except ZeroDivisionError as e:
    print('Division by zero exception')
    z = None
print("Division is : ",z)

***************************
Find Out Type Of Exception:-
***************************

x = input("Enter Number1: ")
y = input ("Enter Number2: ")
try:
    z = int(x)/int(y)
except ZeroDivisionError as e:
    print('Division by zero exception')
	
except Exception as e:
	print('exception type: ',type(e).__name__)
	z = None
print("Division is : ",z)

****************************
User Defind Exception Class:-
****************************

class Accident(Exception):
  def __init__(self,msg):
    self.message=msg
	
  def print_exception(self):
    print("User Defined Exception: ",self.msg)

try:
	raise Accident('Crash between two cars')
except Accident as e:
	e.print_exception()

Output:-
User Defined Exception: Crash between two cars

----------

class Accident(Exception):
	def __init__(self,msg):
		self.message=msg

	def handle(self):
		print("accident occured, take detour")


try:
	raise Accident('crash between two cars')
except Accident as e:
	e.handle()
	
Output:
accident occured, take detour

****************************
Finally Statement :-
****************************
It's difficult to handle all exception , for this we use "Finally" -- if any unhandeled error occurd , , it goes to "Finally" and perform task in finally.

def process_file():
	try:
		f = open("c:\\code\\data.txt")		--data.txt exist on local path.
		x = 1/0
	except FileNotFoundError as e:
		print("cleaning up file")
		f.close()
		
NOTE:- This will through and error because x =1/0 but will not terminate , 
	   it will go into finally and execute close() statement.
	
f.close() -- Will close the file and do some necessary cleanup.