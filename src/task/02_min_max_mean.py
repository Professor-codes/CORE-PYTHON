my_tuple = (10, 20, 30, 40, 50, 60)

if my_tuple:
    minimum = my_tuple[len(my_tuple) - 1]  # index 5 | value 60
    maximum = my_tuple[len(my_tuple) - len(my_tuple)]  # index 0 | value 10
    for numbers in my_tuple:
        if numbers < minimum:
            minimum = numbers
        if numbers > maximum:
            maximum = numbers
    print("Minimum:", minimum)
    print("Maximum:", maximum)
    mean = sum(my_tuple) / len(my_tuple)  # mean = sum of tuple / length of tuple
    print("Mean:", mean)
else:
    print("Tuple is empty.")