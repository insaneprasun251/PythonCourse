# parrot_list = ["non pinin", "no more", "a stiff", "bereft of life"]
#
# parrot_list.append("Norwegian Blue")
# for state in parrot_list:
#     print("This parrot is " + state)
#
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# numbers = even + odd
# numbers.sort()
# print(numbers)
#
# numbers = [even, odd]
#
# for number_set in numbers:
#     print(number_set)
#     for value in number_set:
#         print(value)

menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])

for meal in menu:
    if "spam" not in meal:
        print(meal)
        for ingredient in meal:
            print(ingredient)
