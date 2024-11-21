# NESTED TUPLE
# tuple that contains other tuples as elements
# each nested tuple act as an element of main tuple
# nested_tuple1 = (1, 2, 3, (4, 5, 6))
# print(nested_tuple1)

# INDEXING
#    0   1       2                    main index
x = (1, (2, 3), (4, (5, 6)))
#        0  1    0                    nested index
#                    0  1             sub nested index

# print(x)
print(x[0])  # 1
print(x[1])  # (2, 3)
print(x[2])  # (4, (5, 6))

print(x[1][0])  # 2
print(x[1][1])  # 3

print(x[2][0])  # 4

print(x[2][1][0])  # 5
print(x[2][1][1])  # 6

# PRINT USING LOOP
y = (1, (2, 3), (4, (5, 6)))
for numbers in y:
    if isinstance(numbers, tuple):
        for sub_numbers in numbers:
            print(sub_numbers)
    else:
        print(numbers)

# UNPACKING NESTED TUPLE
z = (10, (20, 30), (40, (50, 60)))
a, (b, c), (d, (e, f)) = z
print(a, b, c, d, e, f)
