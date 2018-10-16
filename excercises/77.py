import datetime

year = datetime.datetime.now().year

x = input("Please enter your age: ")
print("We think you were born in " + str(year - int(x)))
