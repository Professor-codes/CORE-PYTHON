# len()
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(l1))  # Output: 10

# list()
l2 = (99, 88, 77, 66, 55, 44)
print(l2)
print(type(l2)) # <class 'tuple'>
print(list(l2))
print(type(list(l2))) # <class 'LIST'>

l3 = "text"
print(type(l3)) # <class 'str'>
print(list(l3))
print(type(list(l3))) # <class 'list'>

# append()
l4 = [1, 2, 3, 55, 77]
l4.append(99)
l4.append(111)
print(l4)  # Output: [1, 2, 3, 55, 77, 99, 111]

# extend()
l5 = [1, 2, 3, 4, 5]
l5.extend([4, 3, 2, 1])
print(l5)  # Output: [4, 3, 2, 1]

# insert()
l6 = [1, 3, 4]
l6.insert(1, 2)
l6.insert(4, 232)
print(l6)  # Output: [1, 2, 3, 4, 232]

# count()
l7 = [1, 2, 2, 3]
print(l7.count(2))  # Output: 2

# index()
l8 = [1, 2, 3, 4, 5]
print(l8.index(2))  # Output: 1
print(l8.index(4))  # Output: 3

# remove()
l9 = [1, 2, 3]
l9.remove(2)
print(l9)  # Output: [1, 3]

l10 = ["pink", "blue", "orange", "red"]
l10.remove("red")
print(l10) # Output: ['pink', 'blue', 'orange']

# pop()
l11 = [1, 2, 3, 4, 5]
print(l11.pop())   # Output: 5
print(l11)         # Output: [1, 2, 3, 4]

# reverse()
l12 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l12.reverse()
print(l12)  # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# sort()
l13 = [3, 1, 2, 5, 4]
l13.sort()
print(l13)  # Output: [1, 2, 3, 4, 5]

# sorted()
l14 = [3, 1, 2, 5, 4]
print(sorted(l14))  # Output: [1, 2, 3, 4, 5]

# min() max() sum()
l15 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(l15))  # Output: 1
print(max(l15))  # Output: 10
print(sum(l15))  # Output: 55

# nested lists
# index        0   1       2       3      4  5  6   7   8   9
nested_list = [0, [1, 2], [3, 4], [5, 6], 7, 8, 9, [10, 11, 12]]
# index            0  1    0  1    0  1             0   1   2
print(nested_list[0])
print(nested_list[1][0])
print(nested_list[1][1])
print(nested_list[2][0])
print(nested_list[2][1])
print(nested_list[3][0])
print(nested_list[3][1])
print(nested_list[4])
print(nested_list[5])
print(nested_list[6])
print(nested_list[7][0])
print(nested_list[7][1])
print(nested_list[7][2])
