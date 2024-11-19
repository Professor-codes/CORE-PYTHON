# The print() function in Python is used to display output on the console.
# It is one of the most commonly used functions for debugging and showing results.

# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

# objects: One or more values you want to print.
print("Hello, World!")
print("Hello", "Sahil", "Welcome to Python")

# sep: String inserted between values (default: space ' ').
print("Python", "is", "fun", sep="-")  # Output: Python-is-fun

# end: String appended after the last value (default: newline '\n').
print("Hello", end=" ")
print("World!")  # Output: Hello World!

print("Hello")
print("World!")  # by default, it uses '\n'
