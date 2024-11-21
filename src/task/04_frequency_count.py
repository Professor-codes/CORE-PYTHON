my_tuple = (1, 2, 1, 1, 1, 3, 4, 3, 4, 2, 5) # tuple
frequency = {}  # dict

for numbers in my_tuple:
    if numbers in frequency:
        frequency[numbers] += 1
    else:
        frequency[numbers] = 1

for number, count in frequency.items():
    if count <= 1:
        print(f"{number} : {count} time")
    else:
        print(f"{number} : {count} times")
