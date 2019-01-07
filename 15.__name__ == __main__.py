#Value of __name__ is __main__

#Pre defined variable which get set to main

#Entry point of a program in python

print("First Module's Name: {}".format(__name__))
#OUTPUT:- First Module's Name: __main__

#when we import other python file then __name__ sets to that imported module name.

#When we run a file directly , the __name__ will be __main__ , otherwise if we import and run then it will be imported file name.

'''
Every module in python has a special attribute called __name__ .
The value of __name__  attribute is set to '__main__'  when module run as main program.
Otherwise the value of __name__  is set to contain the name of the module.
'''

#Example_REF:- https://thepythonguru.com/what-is-if-__name__-__main__/
#https://www.youtube.com/watch?v=sugvnHA7ElY&index=54&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&t=0s