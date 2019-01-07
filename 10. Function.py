
'''---FUNCTION---POSTITONAL ARG---NAMED ARG---GLOABL VARI---LOCAL VARI---DEFAULT VARI'''
#Functions makes your code more modular
'''
tom_exp_list = [2100,3400,3500]
joe_exp_list = [200,500,700]

total = 0
for items in tom_exp_list:
    total = total + items
print("Tom's Total Exp: " , total)

total = 0
for items in joe_exp_list:
    total = total +items
print("Joe's Total Exp: " , total)

#NOTE:- Problem with this is we are repeating code again and again

#---------------------Same Code using Function----------------------

def calculate_total(exp):
    total = 0
    for items in exp:
        total = total + items
    return total

rudra_exp_list = [1, 2, 3]
Seema_exp_list = [4, 5 , 6]

rudra_total = calculate_total(rudra_exp_list)
seema_total = calculate_total(Seema_exp_list)

print("Rudra's Total Exp: ",rudra_total)
print("Seema's Total Exp: ",seema_total)

#-------------------SUM Using Function-----------------

def sum(a, b):
    Total = a + b
    return Total

n = sum(2,3)
print("Sum of the numbers:", n)

#-------------------Debug Printing---------------------

def sum1(p,q):
    print("first Value inside function to test:", p)
    print("second Value inside function to test:", q)
    Total1 = p + q
    print("total1 inside function:", Total1)
    return Total1

m = sum1(5,6)
print("Total1 outside function: ",m)

#------------------Positional Agruments
#------------------Named Arguments
#We can define it Explecitely while passing by giving name

def sum2(p,q):
    print("first Value inside function to test:", p)
    print("second Value inside function to test:", q)
    Total2 = p + q
    print("total2 inside function:", Total2)
    return Total2

m = sum2(q=5,p=6)
print("Total2 outside function: ",m)

#----------------Global Variable
#----------------Local Variable

#All Variable definced inside a function body are localy accessable
#For Globally defined variable we need to define Variable Outside 

Total3=0                   #Gloabal Variable
def sum3(p,q):
    print("first Value inside function to test:", p)
    print("second Value inside function to test:", q)
    Total3 = p + q          #Local Variable
    print("total3 inside function:", Total3)
    return Total3

m = sum3(q=5,p=6)
print("Total3 outside function: ",m)

print("Global Variable defined here is:",Total3)

#NOTE:- As you can see GLOBAL and LOCAL variables have same name but Values are different

#----------------DEFAULT Arguement

#When we will not pass any value then it will take default value as 10
'''
def sum(x, y=0):           #Default Arg
    Total = x + y
    return Total

z = sum(2)                  # It will take default value 0
z1= sum(2,1)
print("Sum of the numbers:", z)
print("Sum of the numbers:", z1)