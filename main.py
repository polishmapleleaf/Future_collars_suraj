#charecter
from operator import truediv

message = "hello"
print(message)

message = message + " world"
print(message)

#integer

counter = 2
print(counter)

#floating point number

weight_sum = 10.5
print(weight_sum)

#boolean
always_true = True
print(always_true)
never_true = False
print(never_true)

#string
message_2 = "message"

message_3 = """ 
hello 
hello world
123
xyz
"""
print(message_3)

#none
nothing_here = None
print(nothing_here)

#operations on variables
a = 1.5
b = 0.5
print(a+b)
print(a-b)
print(a*b)
print(a/b)

a = 2
b = 3
print(a**b)
print(b%a)

#comparing
print(a == b)
print(a != b)
print( a < b)
print(a <= b)
print(a > b)
print(a >= b)


print("")
#operating with logical (boolean) variables
print(True or False)
print(True or True)
print(False or True)
print(False or False)

print("")
#operating with logical (boolean) variables
print(True and False)
print(True and True)
print(False and True)
print(False and False)

print("")
print(not False)
print(not True)

print("")
#cast to boolean
print(bool(-1))
print(bool(1))
print(bool(0))
print(bool("tekst"))
print(bool(None))

print("")
#check variable type
variable = "text"
print(type(variable))

variable_2 = 123
print(type(variable_2))

print("")
#check variable type
variable = "text"
print(type(variable) is str)


#excersise 1 - swap number
a = input("enter the first number ")
b = input("\nenter the second  number ")
c = b
b = a
a = c
print("\nthe numbers after swapping ", a,",", b)
