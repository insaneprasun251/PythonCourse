while True:
    password = input("Please input password: ")
    if any(i.isdigit() for i in password) and any(i.isupper() for i in password) and len(password) >= 5:
        print("Password is fine")
        break
    else:
        print("Password is not fine")
