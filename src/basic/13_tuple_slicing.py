# slicing is the process of extracting a specific portion of a tuple
# using a range of index
# it creates a new tuple containing the selected elements from the original tuple

# new_tuple = tuple_name[start:stop:step]
# start: The index where slicing begins (inclusive) # Defaults to 0 if omitted
# stop: The index where slicing ends (exclusive)
# step: The interval between elements to include # Defaults to 1 if omitted

# slicing using positive indices
positive = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# index  =  0  1  2  3  4  5  6  7  8  9
print("start from index 0 end to index 9 ->", positive[0:])
print("start from index 0 end to index 4 ->", positive[0:5])
print("start from index 3 end to index 6 ->", positive[3:7])
print("start from index 0 end to index 9 ->", positive[:10])
print("start from index 0 end to index 4 ->", positive[:5])
print("start from index 0 end to index 7 ->", positive[:8])
print("start from index 0 end to index 9 ->", positive[0:10:1])
print("start from index 0 end to index 9 ->", positive[0:10:2])
print("start from index 0 end to index 9 ->", positive[0::5])
print("start from index 0 end to index 6 ->", positive[:7:3])

# slicing using negative indices
negative = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# index  = 10  9  8  7  6  5  4  3  2  1
print("start from index -3 end to index -1 ->", positive[-3:])
print("start from index -10 end to index -3 ->", positive[:-3])
print("start from index -8 end to index -4 ->", positive[-8:-3])
print("start from index -1 end to index -4 ->", negative[-1:-5:-1])
print("start from index -1 end to index -10 ->", negative[::-1])
print("start from index -3 end to index -10 ->", negative[-3::-2])


