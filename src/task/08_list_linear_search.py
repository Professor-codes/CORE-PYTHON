# food_list = ["panner butter masala", "plain naan", "panner tufani", "butter naan"]

food_list = []

n = int(input("food items : "))

for i in range(n):
    food_item = input(f"Enter food item {i + 1}: ")
    food_list.append(food_item)

print(f"food list : {food_list}")

favourite = input("\nyour favourite dish : ")

order = False
for food in food_list:
    if food == favourite:
        order = True
        break

if order:
    print(f"{food} added to cart")
else:
    print(f"Dish not available!")
