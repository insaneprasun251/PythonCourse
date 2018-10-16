while True:
    notes = []
    password = input("Please input password: ")
    if not any(i.isdigit() for i in password):
        notes.append("You need at least one digit")
    if not any(i.isupper() for i in password):
        notes.append("You need at least one Uppercase character")
    if not len(password) >= 5:
        notes.append("Password needs to be at least 5 characters")
    if len(notes) == 0:
        print("Password is fine")
        break
    else:
        print("Check the following: ")
        for note in notes:
            print(note)
