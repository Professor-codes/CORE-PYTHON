# Arithmetic Operators
x = 10
y = 3
print("Arithmetic Operators:")
print("Addition:", x + y)         # 13
print("Subtraction:", x - y)      # 7
print("Multiplication:", x * y)   # 30
print("Division:", x / y)         # 3.333...
print("Modulus:", x % y)          # 1
print("Exponentiation:", x ** y)  # 1000
print("Floor Division:", x // y)  # 3
print()

# Comparison Operators
print("Comparison Operators:")
print("Equal:", x == y)           # False
print("Not Equal:", x != y)       # True
print("Greater than:", x > y)     # True
print("Less than:", x < y)        # False
print("Greater than or equal:", x >= y)  # True
print("Less than or equal:", x <= y)     # False
print()

# Logical Operators
print("Logical Operators:")
a = True
b = False
print("AND:", a and b)            # False
print("OR:", a or b)              # True
print("NOT:", not a)              # False
print()

# Bitwise Operators
print("Bitwise Operators:")
print("AND:", x & y)              # 2
print("OR:", x | y)               # 11
print("XOR:", x ^ y)              # 9
print("NOT:", ~x)                 # -11
print("Left Shift:", x << 2)      # 40
print("Right Shift:", x >> 2)     # 2
print()

# Assignment Operators
print("Assignment Operators:")
z = x
z += y  # z = z + y
print("Add and Assign:", z)       # 13
z *= y  # z = z * y
print("Multiply and Assign:", z)  # 39
print()

# Membership Operators
print("Membership Operators:")
my_list = [1, 2, 3, 4, 5]
print("2 in list:", 2 in my_list)          # True
print("6 not in list:", 6 not in my_list)  # True
print()

# Identity Operators
print("Identity Operators:")
a = [1, 2, 3]
b = [1, 2, 3]
print("a is b:", a is b)          # False (different memory locations)
print("a is not b:", a is not b)  # True
print()

# Ternary Operator
print("Ternary Operator:")
result = "Even" if x % 2 == 0 else "Odd"
print("x is:", result)  # Even
print()
