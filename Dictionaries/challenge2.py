locations = {
    0: {
        "desc": "You are sitting in front of your computer learning Python",
        "exits": {},
        "namedExits": {}
    },
    1: {
        "desc": "You are standing at the end of a road before a small brick building",
        "exits": {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
        "namedExits": {"2": 2, "3": 3, "5": 5, "4": 4}
    },
    2: {
        "desc": "You are at the top of the hill",
        "exits": {"N": 5, "Q": 0},
        "namedExits": {"5": 5}
    },
    3: {
        "desc": "You are inside a building, a well house for a small stream",
        "exits": {"W": 1, "Q": 0},
        "namedExits": {"1": 1}
    },
    4: {
        "desc": "You are in a valley beside a stream",
        "exits": {"N": 1, "W": 2, "Q": 0},
        "namedExits": {"1": 1, "2": 2}
    },
    5: {
        "desc": "You are in a forest",
        "exits": {"W": 2, "S": 1, "Q": 0},
        "namedExits": {"2": 2, "1": 1}
    }

}

words = {
    "QUIT": "Q",
    "WEST": "W",
    "EAST": "E",
    "NORTH": "N",
    "SOUTH": "S"
}

loc = 1
while True:
    availableExits = ""
    for direction in locations[loc]['exits'].keys():  # Iterates through the keys in exits list with index 1 (loc)
        availableExits += direction + ", "  # Adds every available exits to the variable

    print(locations[loc]['desc'])  # Prints description of a locations based on key (loc)

    if loc == 0:  # If chosen Q it goes to the location O, prints the value associated with the key and exits
        break

    direction = input("Available exits are: " + availableExits + " ").upper()
    if len(direction) > 1:  # more than one letter, so check words
        for word in words:  # does it contain a word we know?
            # print(word)
            if word in direction:
                direction = words[word]
                # print(direction)

    print()   # Prints empty line
    if direction in locations[loc]['exits']:  # if input is in a list of exits for that location (loc)
        loc = locations[loc]['exits'][direction]  # loc is changed to be a value of that direction key in a exits list
    else:
        print("You cannot go in that direction")