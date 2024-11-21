# concatenation is the process of combining two or more tuples
# into a single tuple using the + operator

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6, 90)
combine_tuple1_tuple2 = tuple1 + tuple2
print(combine_tuple1_tuple2)  # (1,2,3,4,5,6,90)

empty_tuple = ()
nonempty_tuple = (9, 8, 7, 6, 5, 4, 3, 2, 1)
joinTuple = empty_tuple + nonempty_tuple
print(joinTuple)  # (9, 8, 7, 6, 5, 4, 3, 2, 1)

t1 = (12, 3.14, "car", "bike")
t2 = ("red", "magenta")
t3 = ("laptop", "headphone")
newTuple = t1 + t2 + t3
print(newTuple) # (12, 3.14, 'car', 'bike', 'red', 'magenta', 'laptop', 'headphone')