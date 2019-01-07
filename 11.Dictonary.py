d = {"tom":9650333146, "rob":9850444456, "joe":7659907654}

print(d)

#Accessing values from dictonary

print(d["tom"])

#Adding values in dictonary

d["seema"]=9866789065

print(d)

#Deleating Values from dictonary

del d["seema"]

print(d)

#Print all dict Values

for key in d:
    print("Key is:",key,"And Value is:",d[key])

#Another way

for k,v in d.items():
    print("Key is:",k,"And Value is:",v)

# check something present in Dictonary

print('samir' in d)

print('joe' in d)

# Deleting all values from dictonary

d.clear()

print(d)