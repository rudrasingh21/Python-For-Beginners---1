num = input("Enter a number")
num = int(num)
if num % 2==0:
    print("Number is Even")
else:
    print("Number is odd")

#Small Program using IF

indian=["samosa","daal","naan"]
chinese=["egg role","pot sticker","fried rice"]
italian=["pizza","pasta","risotto"]

dish = input("Enter a dish name: ")

if dish in indian:
    print("indian")
elif dish in chinese:
    print("chinese")
elif dish in italian:
    print("italian")
else:
    print("I don't know which cuisine is this ",dish)