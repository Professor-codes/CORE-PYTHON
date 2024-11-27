# numbers = [1, 1, 1, 2, 2, 3]
# frequency = {}
#
# for num in numbers:
#     frequency[num] = frequency.get(num, 0) + 1
#     print(frequency[num])
#
# print(f"frequency count -> {frequency}")


my_list = [1, 2, 1, 1, 1, 3, 4, 3, 4, 5] # list
frequency = {}  # dict

for numbers in my_list:
    if numbers in frequency:
        frequency[numbers] += 1
    else:
        frequency[numbers] = 1

for number, count in frequency.items():
    if count <= 1:
        print(f"{number} : {count} time")
    else:
        print(f"{number} : {count} times")
