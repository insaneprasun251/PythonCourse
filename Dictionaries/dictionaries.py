fruit = {
        "orange": "a sweet, orange, citrus fruit",
        "apple": "good for making cider",
        "lemon": "a sour, yellow citrus fruit",
        "grape": "a small, sweet fruit growing in bunches",
        "lime": "a sour, green citrus fruit"
}

# print(fruit)
# print(fruit["lemon"])
# fruit["pear"] = "an odd shaped apple"
# print(fruit["pear"])
# del fruit["lemon"]
# print(fruit)
# print(fruit)
while True:
    dict_key = input("Please enter fruit: ")
    if dict_key == "quit":
        break
    if dict_key in fruit:
        description = fruit.get(dict_key)
        print(description)
    else:
        print("We don't have a " + dict_key)
        break

# for snack in fruit:
#     print(fruit[snack])
k = "tomato"
print(k in fruit)   # Checks if a key is in a dictionary and returns boolean

print(fruit.keys())
print(fruit.values())
print(fruit.items())
