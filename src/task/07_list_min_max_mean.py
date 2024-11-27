number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

min = number_list[0] # 1
max = number_list[0] # 1

for number in number_list:
    if number < min:
        min = number
    if number > max:
        max = number
    mean = sum(number_list) / len(number_list)

print(f"min : {min}")
print(f"max : {max}")
print(f"mean : {mean}")
