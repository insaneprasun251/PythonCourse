shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shopping_list:
    if item == "spam":
        print("I'm ignoring " + item)
        continue  # bypasses item found and goes to another one
    print("Buy " + item)

print("New shopping list:")
for item in shopping_list:
    if item == "spam":
        break
    print("Buy " + item)

meal = ["egg", "bacon", "tomato", "sausages"]
nasty_food_item = ''
for item in meal:
    if item == "spam":
        nasty_food_item = item
        break

if nasty_food_item:
    print("Can't I have anything without spam in it")
else:  # else here cause inside the for loop it would be printed x times based on number of items in meal
    print("I'll have a plate of that please!")