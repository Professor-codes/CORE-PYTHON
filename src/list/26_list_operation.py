# concatenation
l1 = [1, 2, 3]
l2 = [4, 5, 6]
result = l1 + l2
print(result)  # Output: [1, 2, 3, 4, 5, 6]

# repetition
l3 = [1, 2, 3]
result = l3 * 2
print(result)  # Output: [1, 2, 3, 1, 2, 3]

# membership
l4 = [1, 2, 3, 5, 7, 9]
print(2 in l4)   # Output: True
print(4 in l4)   # Output: False

# slicing
l5 = [10, 20, 30, 40, 50]
#      0   1   2   3   4
print(l5[1:4])  # Output: [20, 30, 40]
print(l5[:3])   # Output: [10, 20, 30]
print(l5[::2])  # Output: [10, 30, 50]
print(l5[::4])  # Output: [10, 50]


