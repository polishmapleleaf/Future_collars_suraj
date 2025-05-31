# 9.Logical Operators: and, or
# Use boolean variables (e.g. is_password_correct, is_username_correct) and combine them with logical operators to simulate login access logic.

is_username_correct = False
is_password_correct = True
if not is_username_correct and not is_password_correct:
    print("please enter correct user name and password")
elif not is_password_correct or not is_username_correct:
    print(" please enter correct user name or password")
else:
    print("access is granted ")
