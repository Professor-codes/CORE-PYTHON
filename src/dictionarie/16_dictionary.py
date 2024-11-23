# dictionaries are used to store data in key:value pairs
# dictionary is a collection which is ordered, changeable
# and do not allow duplicates
colorDict = {
    "pink": "magenta",
    "code1": "#FF00FF",
    "purple": "blueviolet",
    "code2": "#8A2BE2",
    "green": "springgreen",
    "code3": "#00FF7F",
}
print(colorDict)

# using dict() constructor to create dictionary
person = dict(name="Alexa", age=22, country="USA")
print(person)

# duplicate values will overwrite existing values
product = {
    "name": "Immortal 131",
    "brand": "Boat",
    "year": 2016,
    "year": 2022,
}
print(product)

# values in dictionary items can be of any data type
food = {
    "name": "burger",
    "price": 80,
    "type": ["veg", "non-veg"],
}
print(food)
