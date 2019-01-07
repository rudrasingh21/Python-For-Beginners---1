f=open("c://data//book.txt","r")
s=f.read()
print(s)    #Will give a result as string

#Above will print all data in book.txt

import json
book=json.loads(s)
print(book) #will give result as dictonaty

# now you can access JSON as DICT

print(book['bob'])

print['bob']['phone']