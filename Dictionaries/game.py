locations = {
    0: "You are sitting in front of your computer learning Python",
    1: "You are standing at the end of a road before a small brick building",
    2: "You are at the top of the hill",
    3: "You are inside a building, a well house for a small stream",
    4: "You are in a valley beside a stream",
    5: "You are in a forest"
}

exits = {
    0: {"Q": 0},
    1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
    2: {"N": 5, "Q": 0},
    3: {"W": 1, "Q": 0},
    4: {"N": 1, "W": 2, "Q": 0},
    5: {"W": 2, "S": 1, "Q": 0}
}

namedExits = {
    1: {"2": 2, "3": 3, "5": 5, "4": 4},
    2: {"5": 5},
    3: {"1": 1},
    4: {"1": 1, "2": 2},
    5: {"2": 2, "1": 1}
}

words = {
    "QUIT": "Q",
    "WEST": "W",
    "EAST": "E",
    "NORTH": "N",
    "SOUTH": "S",
    "ROAD": "1",
    "HILL": "2",
    "BUILDING": "3",
    "VALLEY": "4",
    "FOREST": "5"
}

loc = 1
while True:
    availableExits = ""
    for direction in exits[loc].keys():  # Iterates through the keys in exits list with index 1 (loc)
        availableExits += direction + ", "  # Adds every available exits to the variable

    print(locations[loc])  # Prints description of a locations based on key (loc)

    if loc == 0:  # If chosen Q it goes to the location O, prints the value associated with the key and exits
        break
    else:
        allExits = exits[loc].copy()
        allExits.update(namedExits[loc])

    direction = input("Available exits are: " + availableExits + " ").upper()
    if len(direction) > 1:  # more than one letter, so check words
        for word in words:  # does it contain a word we know?
            # print(word)
            if word in direction:
                direction = words[word]
                # print(direction)

    print()   # Prints empty line
    if direction in allExits:  # if input is in a list of exits for that location (loc)
        loc = allExits[direction]  # loc is changed to be a value of that direction key in a exits list
    else:
        print("You cannot go in that direction")