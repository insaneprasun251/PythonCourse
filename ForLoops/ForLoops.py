number = "12434354674654354322131443659089076"
cleanedNumber = ''

for char in number:
    if char in '0123456789':
        cleanedNumber = cleanedNumber + char
newNumber = int(cleanedNumber)
print ("The number is {}".format(newNumber))

for state in ("not pinin'", "no more", "a stiff", "bereft of life"):
    print("This parrot is " + state)
    print("This parrot is {}".format(state))

for i in range (0, 100, 5):
    print("i is {}".format(i))

for i in range(1,13):
    for j in range(1,13):
        print(("{1} times {0} is {2}".format(i, j, i*j)), end='\t')
    print