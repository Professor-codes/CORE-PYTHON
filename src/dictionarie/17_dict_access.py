person = {
    "name": "Alexa",
    "age": 22,
    "country": "USA",
}
# print(person)

# access the dictionary using square bracket with key reference
print(person["name"])
print(person["age"])
print(person["country"])

# access the dictionary using get method
person_name = person.get("name")
person_age = person.get("age")
person_country = person.get("country")
print(f"Name : {person_name}")
print(f"Age : {person_age}")
print(f"Country : {person_country}")