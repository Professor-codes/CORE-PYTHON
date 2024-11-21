# membership testing in tuples is performed using the
# in and not in operators
# it will check if a specific value exists in the tuple
# and return a boolean value true or false
# in: returns true if value exists, otherwise false
# not in: returns true if value does not exist, otherwise false

num_tuple = (10, 20, 30, 40, 50, 60, 70, 80)
print("10 in num_tuple :", 10 in num_tuple) # True
print("99 in num_tuple :", 99 in num_tuple) # False

print("99 not in num_tuple :", 99 not in num_tuple) # True
print("10 not in num_tuple :", 10 not in num_tuple) # False