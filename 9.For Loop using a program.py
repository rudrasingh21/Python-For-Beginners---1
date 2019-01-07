#Without sing FOR Loop
exp = [2340,2500,1222,4533]
total = exp[0]+exp[1]+exp[2]+exp[3]
print("Total exp is:", total)

#Using FOR Loop

exp1 = [2340,2500,1222,4533]
for items in exp1:
    All_total = total + items
print(All_total)

#Use range in for loop

for i in range(1,11):
    print(i*i)

#Print Month Number and Expence and in the end Print total expense

exp2 = [2340,2500,1222,4533]
for i in range (len(exp2)):
    print("Month:",(i+1),"Expences:",exp2[i])
    total = total + exp2[i]
print("My Total Exp is:",total)