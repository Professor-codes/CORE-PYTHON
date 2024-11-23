# traversing is visiting each key-value pair in order
sample1 = {
    "a": 1,
    "b": 2,
    "c": 3,
}
print(sample1)

# traverse only keys
for key in sample1.keys():
    print(key)

# traverse only values
for value in sample1.values():
    print(value)

# traverse keys and values
for key_value in sample1.items():
    print(key_value)

# traverse with index and item using enumerate
for index, item in enumerate(sample1.items()):
    print(f"index : {index}, item : {item}")

# traverse with index, key and value using enumerate
for index, key in enumerate(sample1):
    print(f"index : {index}, key : {key}, value : {sample1[key]}")
