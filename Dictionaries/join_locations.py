locations = {
    0: "You are sitting in front of your computer learning Python",
    1: "You are standing at the end of a road before a small brick building",
    2: "You are at the top of the hill",
    3: "You are inside a building, a well house for a small stream",
    4: "You are in a valley beside a stream",
    5: "You are in a forest"
}

exits = [
    {"Q": 0},
    {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
    {"N": 5, "Q": 0},
    {"W": 1, "Q": 0},
    {"N": 1, "W": 2, "Q": 0},
    {"W": 2, "S": 1, "Q": 0}
]

loc = 1
while True:
    availableExits = ""
    for direction in exits[loc].keys():  # Iterates through the keys in exits list with index 1 (loc)
        availableExits += direction + ", "  # Adds every available exits to the variable

    print(locations[loc])  # Prints description of a locations based on key (loc)

    if loc == 0:  # If chosen Q it goes to the location O, prints the value associated with the key and exits
        break

    direction = input("Available exits are: " + availableExits.upper())
    print()   # Prints empty line
    if direction in exits[loc]:  # if input is in a list of exits for that location (loc)
        loc = exits[loc][direction]  # loc is changed to be a value of that direction key in a exits list
    else:
        print("You cannot go in that direction")
