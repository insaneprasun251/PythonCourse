known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]

# for name in known_users:
#     known_users[known_users.index(name)] = name.lower()
#
# print(known_users)

while True:
    print("Hi! My name is Travis")
    user = input("What is your name? ").capitalize()
    if user in known_users:
        print("Hello {}!".format(user))
        remove = input("Would you like to be removed from the system (y/n)?: ").lower()
        if remove == 'y':
            known_users.pop(known_users.index(user.capitalize()))
            print(known_users)
        elif remove == 'n':
            print("No problem, I didn't want you to leave anyway!")
        break
    else:
        print("User not recognized")
        add = input("Would you like to be added to the system (y/n)?: ").lower()
        if add == 'y':
            known_users.append(user.capitalize())
            print(known_users)
        elif add == 'n':
            print("That's a shame!")
        break

