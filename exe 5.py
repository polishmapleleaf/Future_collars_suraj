#5.Simple Calculator
#Declare two numbers (x, y) and print the result of basic operations: addition, subtraction, multiplication, and division.

x = int(input("enter the first number "))
y = int(input("enter the second number "))
z = str(input("please tell me what operation you want to do "))
if z=="addition" or z=="+":
    print("\n the sum is ", x+y)
elif z=="subtraction" or z=="-":
    print(" the subraction is ", x-y)
elif z=="multiplication" or z=="*":
    print(" the multiplication is ", x*y)
elif z=="division" or z=="/":
    print("the division is ", x/y)
else:
    print("currectly specify the calculation")