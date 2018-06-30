def display_names(first, second):
    print(f"{first} says hello to {second}")


names = {"first": "Colt", "second": "Steele"}

display_names(**names)
