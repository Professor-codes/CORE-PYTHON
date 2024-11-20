# INT
# int() convert a value into an integer
# used with numbers, strings, or objects that implement a __int__() method
# SYNTAX
# int(x=0, base=10)
print(int())  # Output: 0 (defaults to 0 if no argument is provided)
print(int(13))  # Output: 13

# FLOAT
# float() convert a value to a floating-point number (decimal)
# handle integers, strings, or other objects that define a __float__() method
# SYNTAX
# float(x=0)
print(float())  # Output: 0.0
print(float(5))  # Output: 5.0

# STR
# str() convert a given object to its string representation
# handle numbers, collections (e.g., lists, tuples), or any object that implements the __str__() or __repr__() method
# SYNTAX
# str(object='')
print(str(123))  # Output: '123'
print(str(-8))  # Output: '-8'

# ORD
# used to return the Unicode code point (an integer) for a given character
# SYNTAX
# ord(character)
print(ord('A'))  # Output: 65
print(ord('0'))  # Output: 48
print(ord('$'))  # Output: 36
print(ord('\n')) # Output: 10
print(ord('π'))  # Output: 960
print(ord('💻')) # Output: 128187

# HEX
# used to convert an integer to its corresponding hexadecimal string representation
# resulting string starts with the prefix 0x
# indicating that it is a hexadecimal number
# SYNTAX
# hex(x)
print(hex(255))  # Output: '0xff'
print(hex(16))   # Output: '0x10'

# OCT
# used to convert an integer to its octal string representation
# resulting string begins with the prefix 0o
# indicating it is an octal number
# SYNTAX
# oct(x)
print(oct(8))    # Output: '0o10'
print(oct(64))   # Output: '0o100'
print(oct(-8))   # Output: '-0o10'
print(oct(-65))  # Output: '-0o101'
print(oct(0))  # Output: '0o0'




