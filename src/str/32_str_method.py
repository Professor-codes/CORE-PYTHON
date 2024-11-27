s1 = "lorem ipsum dolar SIT"

print(s1)

# len(): Returns the length of the string
print(len(s1))  # Output: 23

# capitalize(): Capitalizes the first character of the string
print(s1.capitalize())

# title(): Capitalizes the first character of each word
print(s1.title())

# lower(): Converts the string to lowercase
print(s1.lower())

# upper(): Converts the string to uppercase
print(s1.upper())

# count(): Returns the number of occurrences of a substring in the string
print(s1.count("a"))

# find(): Returns the lowest index of the substring if it is found in the string; returns -1 if not found
print(s1.find("e"))

# index(): Same as find() but raises a ValueError if the substring is not found
print(s1.index("dolar"))

# endswith(suffix[, start[, end]]): Checks if a string ends with a specified suffix
print(s1.endswith("SIT"))  # Output: True
print(s1.endswith("sit"))  # Output: False

# startswith(prefix[, start[, end]]): Checks if a string starts with a specified prefix
print(s1.startswith("lorem"))  # Output: True
print(s1.startswith("LOREM"))  # Output: True

# isalnum(): Returns True if all characters are alphanumeric
print(s1.isalnum())  # Output: False
print('abc123'.isalnum())  # Output: True

# isalpha(): Returns True if all characters are alphabetic
print(s1.isalpha())  # Output: False
print('abc'.isalpha())  # Output: True

# isdigit(): Returns True if all characters are digits
print(s1.isdigit())  # Output: False
print("1234".isdigit())  # Output: True

# islower(): Returns True if all characters are lowercase
print(s1.islower()) # Output: False
print("hello".islower())  # Output: True

# isupper(): Returns True if all characters are uppercase
print(s1.isupper()) # Output: False
print("HELLO".isupper())  # Output: True

# isspace(): Returns True if the string contains only whitespace
print(s1.isspace())  # Output: False
print(" ".isspace())  # Output: True

# lstrip([chars]): Removes leading whitespace or specified characters
print("  hello".lstrip())  # Output: "hello"

# rstrip([chars]): Removes trailing whitespace or specified characters
print("hello  ".rstrip())  # Output: "hello"

# strip([chars]): Removes both leading and trailing whitespace or specified characters
print("  hello  ".strip())  # Output: "hello"

# replace(old, new[, count]): Replaces occurrences of old with new
print("try".replace("t", "f"))  # Output: "fry"

# join(iterable): Joins elements of an iterable with the string as a separator
print(", ".join(["apple", "banana"]))  # Output: "apple, banana"

# partition(sep): Splits the string into a tuple (head, sep, tail) at the first occurrence of sep
print("hello world".partition(" "))  # Output: ('hello', ' ', 'world')

# split(sep=None, maxsplit=-1): Splits the string into a list using the specified sep
print("a,b,c".split(","))  # Output: ['a', 'b', 'c']