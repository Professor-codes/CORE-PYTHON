text = input("text : ")
charcount = {}

for char in text:
    if char in charcount:
        print(char)
        charcount[char] += 1  # if the character is already in the dictionary, increment the count
    else:
        print(char)
        charcount[char] = 1  # if the character is not in the dictionary, add it with a count of 1

print(f"character counts : {charcount}")
