# len()
# returns the number of key-value pairs in a dictionary
my_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}
print(len(my_dict))

# dict()
# Create a dictionary
new_dict = dict(a=1, b=2, c=3)
print(new_dict)

# keys()
# returns all the keys in the dictionary
sample = {
    'a': 1,
    'b': 2,
    'c': 3
}
print(sample.keys())

# values()
# returns all the values in the dictionary
print(sample.values())

# items()
# returns all the key-value pairs in the dictionary
print(my_dict.items())

# get(key, default=None)
# returns the value for the specified key
# or default if the key is not found
person = {
    "name": "Alexa",
    "age": 22,
    "country": "USA",
}
print(person.get("name"))
print(person.get("age"))
print(person.get("country"))
# value not present
print(person.get("id"))  # Output: None (default behavior if key is missing)
# should not be named explicitly as default
print(person.get("car", "currently, i don't have any car"))  # Output: currently, I don't have any car

# update()
# dictionary with key-value pairs from another dictionary or an iterable
signal = {
    "1": "red",
    "2": "yellow",
    "3": "green",
}
print("simple signal ->", signal)

signal.update({"4": None, "5": None})
print("update signal ->", signal)

other_signal = {
    "6": "black",
    "7": "white"
}
print("other signal ->", other_signal)

signal.update(other_signal)
print("final signal ->", signal)

# del
# delete a key-value pair by key
order = {
    "p1": "iphone 16",
    "p2": "macbook air m4",
    "p3": "mac pro"
}
print(order)

del order["p3"]
print(order)

# clear()
# removes all key-value pairs from the dictionary
data = {
    "d1": "movie",
    "d2": "image",
    "d3": "software",
}
print(data)
print(data.clear())  # Output: {}
print("Drive is successfully cleanup :)")

# fromkeys(keys, value=None)
# creates a new dictionary with specified keys and an optional value
random_keys = ['key166', 'key432', 'key929']
new_dict1 = dict.fromkeys(random_keys)
print(new_dict1)  # Output: {'key166': None, 'key432': None, 'key929': None}
new_dict2 = dict.fromkeys(random_keys, "*")
print(new_dict2)  # Output: {'key166': '*', 'key432': '*', 'key929': '*'}

# copy()
# creates a shallow copy of the dictionary
first = {
    "greet": "Hi",
    "name": "Alexa"
}
second = first.copy()
print(second)

# pop(key, default=None)
# removes and returns the value for the specified key
# or returns default if the key does not exist
bag = {
    "item1": "books",
    "item2": "pencil",
    "item3": "laptop",
    "item4": "ipad",
}
print(bag)

remove_laptop = bag.pop("item3")  # laptop
print(remove_laptop)
print(bag)  # Output: {'item1': 'books', 'item2': 'pen', 'item4': 'ipad'}

remove_books = bag.pop("item1")  # books
print(remove_books)
print(bag)  # Output: {'item2': 'pencil', 'item4': 'ipad'}

# popitem()
# removes and returns the last inserted key-value pair
lunchbox = {
    "item1": "Veggie Wraps",
    "item2": "Rice Bowl",
    "item3": "Rice Bowl",
    "item4": "Pasta Salad",
    "item5": "Stuffed Samosa",
    "item6": "Mini Sandwiches",
}
print(lunchbox)

remove_mini_sandwiches = lunchbox.popitem()
print("removed mini sandwiches :", remove_mini_sandwiches)
print(lunchbox)
remove_stuffed_samosa = lunchbox.popitem()
print("removed stuffed samosa :", remove_stuffed_samosa)
print(lunchbox)

# setdefault()
# used with dictionaries
# returns the value of a specified key
# key does not exist inserts the key with a specified default value
nums = {'first': 1, 'second': 2, 'third': 3}
check1 = nums.setdefault('first', 0)
print(nums)
print(check1)
check2 = nums.setdefault('fourth', 4)
print(nums)
print(check2)
check3 = nums.setdefault('fiftyfive', 55)
print(nums)
print(check3)

# max()
# returns the largest item in an iterable or
# the largest of two or more arguments
l1 = [4, 6, 8, 8, 3, 54, 6, 2, 5]
print(max(l1))  # 54
# key=len is specified
# max compares the length of each string
l2 = ['maxim', 'zia', 'john', 'sara']
print(max(l2, key=len))  # returns maxim, because max length = 5
# by default
# max compares the strings in lexicographically, alphabetical order
print(max(l2))  # returns zia, because z is occurring last in alphabetical order
l3 = max(20, 40, 60, 88, 99)
print(l3)

# min()
# returns the smallest item in an iterable or
# the smallest of two or more arguments
t1 = (4, 6, 8, 8, 3, 54, 6, 2, 5)
print(min(t1))
# key=len is specified
# min compares the length of each string
t2 = ('maxim', 'zia', 'john', 'sara')
print(min(t2, key=len))  # returns zia, because min length = 3
# by default
# min compares the strings in lexicographically, alphabetical order
print(min(t2))  # returns john, because j is occurring first in alphabetical order
t3 = min(20, 40, 60, 88, 99)
print(t3)

# sorted()
# returns a new sorted list from the elements of an iterable
t4 = (8, 3, 1, 7, 2, 5, 4, 6)
print(t4)
print(type(t4))  # <class 'tuple'>
print(sorted(t4))
print(type(sorted(t4)))  # <class 'list'>
# sorting in reverse order
print(sorted(t4, reverse=True))
# by default reverse is false
print(sorted(t4, reverse=False))
# sorting with key
t5 = ("cat", "danger", "ball", "eat", "air")
print(t5)
# by default sorting order is alphabetical order
print(sorted(t5))
# using key length sorting
print(sorted(t5, key=len))  # ordering sequence is depending on length of string

# merging dict
first = {"greet": "Hi"}
second = {"name": "Alexa"}
merged = first | second  # Python 3.9+
print(merged)  # Output: {'greet': 'Hi', 'name': 'Alexa'}
