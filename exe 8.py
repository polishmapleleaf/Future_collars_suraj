#8.Boolean Variable and not Operator
#Create a boolean variable like is_logged_in = False, then use the not operator to take action if the condition is not met.

is_logged_in = False

if not is_logged_in:
    print("access denied, please log in first")
else:
    print("welcome you are logged in")