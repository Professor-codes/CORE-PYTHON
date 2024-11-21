my_tuple = (10, 20, 30, 40, 50, 60)
# index  =   0   1   2   3   4   5
number = 30

found = False
for index in range(len(my_tuple)):
    if my_tuple[index] == number:
        found = True
        print(f"{number} found at index: {index}")
        break
if not found:
    print(f"{number} not found:)")

# m = (1, 2, 3, 4, 5)
# for i in m:  # returns value
#     print(i)
# for i in range(len(m)):  # returns index
#     print(i)
