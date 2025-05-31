# 10.Check If Number Is Within a Range
# Create a variable number and use logical operators to check if it's between 10 and 20 (inclusive).

a = int(input("enter the number "))
if 10 <= a and 20>=a:
    print(a, " is within the range of 10 to 20 ")
else:
    print(a," is not within the range of 10 to 20 ")