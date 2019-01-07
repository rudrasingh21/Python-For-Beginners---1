f = open("C:\\Users\\test.txt","w")
f.write("I love python")
f.close()

#Append

f = open("C:\\Users\\test.txt","a")
f.write("\nI love php")
f.close()

#Reading file line by line

f = open("C:\\Users\\test.txt","r")
print(f.read())
f.close()

#Now count number of words in each line

f = open("C:\\Users\\test.txt","r")
f_out = open("C:\\Users\\test_out.txt","w")
for line in f:
    tokens = line.split(' ')
#    print(str(tokens))      #this will print all the words in each line
#    print(len(str(tokens)))
     f_out.write(line+" Word_count is : "+str(len(tokens)))
     f_out.close()

#To check if a file is closed or not

print(f.close)