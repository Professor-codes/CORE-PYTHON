# len()
# returns number of element or length of tuple
t1 = (1, 2, 3, 4, 5, 6)
print(len(t1))  # 6
t2 = (19, 45, "food", "newspaper", 3.14)
print(len(t2))  # 5
t3 = (3.14, 6.99, 45, 67, "one", "nine", ("ten", "zero"), "red", "purple", ("numpy", "pandas"))
print(len(t3))  # 10

# tuple()
# converts list, string into a tuple
l1 = [1, 2, 3, 4, 5]
print(l1)
print(type(l1))  # <class 'list'>
x1 = tuple(l1)
print(x1)
print(type(x1))  # <class 'tuple'>

# count()
# count the number of times a specific value appears
c1 = (11, 22, 33, 44, 22, 22, 55, 88, 99, 33, 99)
print(c1.count(11))  # 1
print(c1.count(22))  # 3
print(c1.count(33))  # 2
print(c1.count(44))  # 1
print(c1.count(55))  # 1
print(c1.count(88))  # 1
c2 = ("mumbai", "chennai", "gandhi nagar", "pune", "mumbai", "chennai", "goa", "mumbai")
print("count :", c2.count(input("enter city : ")))

# index()
# find the first index of a specified value in the tuple
# if the value is not found
# it raises a ValueError
# tuple.index(value, start=0, end=len(tuple))
# value: item whose index you want to find
# start (optional): index where the search starts (default is 0)
# end (optional): index where the search ends (default is the length of the tuple)
i1 = (1, 2, 3, 4, 5, 2, 9, 4, 6, 8, 9)
print("2 present at index :", i1.index(2))
print("4 present at index :", i1.index(4))

# sorted()
# sort the elements of a tuple in ascending or descending order
# tuples are immutable (cannot be modified directly)
# the sorted() function returns a new list
# that contains the sorted elements, not a sorted tuple
# sorted(iterable, key=None, reverse=False)
# iterable: The iterable (like a tuple) to be sorted
# key (optional): function to execute on each element before sorting # Default is None
# reverse (optional): if true the list is sorted in descending order # Default is False
s1 = (7, 3, 6, 1, 9, 4, 2, 5, 8)
print("unsorted:", s1)
print(type(s1))  # <class 'tuple'>
print("sorted:", sorted(s1))
print(type(sorted(s1)))  # <class 'list'>
# s1 result is a list not a tuple
# if you want the result as a tuple
# you can convert the list back to a tuple
s2 = (70, 30, 60, 10, 90, 40, 20, 50, 80)
print("unsorted:", s2)
print(type(s2))  # <class 'tuple'>
print("sorted:", tuple(sorted(s2)))
print(type(tuple(sorted(s2))))  # <class 'tuple'>

# min()
# find the smallest element in a tuple
print(min(9, 8, 7, 6))  # 6
min1 = (12, 45, 67, 234, 56, 2, 57, 99, 354)
print(min(min1))  # 2

# max()
# find the largest element in a tuple
print(max(1, 2, 3, 4))  # 4
max1 = (12, 45, 67, 234, 56, 2, 57, 99, 354)
print(max(max1))  # 354

# sum()
# calculate the sum of elements
sum1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(sum(sum1))  # 55
sum2 = (1, 1)
print(sum(sum2, 100))  # 2 + 100 = 102

# tuple assignment
# powerful and clean way to unpack values
# from tuples, iterables, or even nested structures
a, b, c = (55, 72, 49)
print(a)  # 55
print(b)  # 72
print(c)  # 49
ta1 = (1, 2, 3, 88, 99)
p, q, r, s, t = ta1
print(ta1)
print(p, q, r, s, t)
# p, q = t      # ValueError: too many values to unpack (expected 3)