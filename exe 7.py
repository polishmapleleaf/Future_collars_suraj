# 7.Compare Values
# Create two variables and compare them using comparison operators (>, <, ==, !=). Print the results.

a = int(input("enter the first value "))
b = int(input("enter the second value "))
if a == b:
    print(a, "is equal to ",b)
elif a < b:
    print(a, " is lessthan ",b)
elif a > b:
    print(a," is greaterthan ",b)
