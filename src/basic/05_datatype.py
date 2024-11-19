# Numeric Types
x = 10          # int
y = 3.14        # float
z = 2 + 3j      # complex
print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'float'>
print(type(z))  # Output: <class 'complex'>
print(end="\n")

# Sequence Types
s = "Python"        # str - immutable sequence of characters
lst = [1, 2, 3]     # list - ordered, mutable collection of items
tup = (4, 5, 6)     # tuple - ordered, immutable collection of items
print(type(s))      # Output: <class 'str'>
print(type(lst))    # Output: <class 'list'>
print(type(tup))    # Output: <class 'tuple'>
print(end="\n")

# Mapping Type
d = {"name": "Sahil", "age": 25}      # dict - unordered, mutable collection of key-value pairs
print(type(d))                        # Output: <class 'dict'>
print(end="\n")

# Set Types
st = {1, 2, 3}          # set - unordered, mutable, no duplicate values
fs = frozenset([4, 5])  # frozenset - immutable version of a set
print(type(st))         # Output: <class 'set'>
print(type(fs))         # Output: <class 'frozenset'>
print(end="\n")

# Boolean Type
x = True
y = False
print(type(x))  # Output: <class 'bool'>
print(type(y))  # Output: <class 'bool'>
print(end="\n")

# None Type
p = None
print(type(p))  # Output: <class 'NoneType'>
print(end="\n")

# Type Conversion
# Function	Converts to  	Example
# int()	    Integer	        int(3.14) → 3
# float()	Floating-point	float(10) → 10.0
# str()	    String	        str(10) → "10"
# list()	List	        list((1, 2, 3)) → [1, 2, 3]
# tuple()	Tuple	        tuple([1, 2, 3]) → (1, 2, 3)
# set()	    Set	            set([1, 2, 3]) → {1, 2, 3}
# dict()	Dictionary	    dict([(1, "a"), (2, "b")])


