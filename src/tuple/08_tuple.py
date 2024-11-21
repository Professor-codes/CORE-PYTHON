# used to store multiple items in a single variable
# ordered, unchangeable, allow duplicate values
# written within round brackets

# SYNTAX
myTuple = ("apple", "banana", "cherry")
print(myTuple)

# UPDATE
# convert the tuple into a list to be able to change it
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print("update kiwi replace banana -> ", x)

# REMOVE
# convert the tuple into a list, remove "apple", and convert it back into a tuple
x = ("apple", "banana", "cherry")
y = list(x)
y.remove("apple")
x = tuple(y)
print("remove apple -> ", x)

# UNPACK
# extract the values back into variables, called unpacking
fruits = ("apple", "banana", "cherry")
(x, y, z) = fruits
print(x)
print(y)
print(z)

# LOOP
name = ("alex", "jena", "maxim")
for x in name:
    print(x)


