# Calculations
var = (25 * 15 + 33) / 2.0
print (var)
# Strings
string = 'I am a basic string'
print (string)
# Replacing
word = "Ford"
word = 'L' +word[1:]
print(word)
# Length of the strings
var2 = len('My length is enormous')
print ('The length of the statement is {y}'.format(y = var2))
# Escape characters
print ('I\'m a string in "Python" ')
print (r'c:\system\nan')
print ("""\
        Hello:
                It is user defined output with triple quotes
            """)
# Booleans (TRUE and FALSE)
print (5 < 6)
print (10 > 15)
print (2 >= 5)
print (4 != 2)
print ("abc" == "abc")
a = True
b = False
print (not a)

# If statement
passerby_speech = 'Hiho'
if passerby_speech == 'Hi' or passerby_speech == 'Hello':
    print ("Hello, how are you doing?")
elif passerby_speech == 'Hey':
    print ("Hi")
else:
    print ("I don't know you!")

if 5 < 7 :
    if 6 > 4:
            print ("6 > 4")
num = 6
if num > 3 & num <= 5:
    print ('Number is 5')
else:
    print ('Number is not 5')
# Turning operator (the value of a will be 7 if the condition is true or 14 if it is false)
a = 3
a = 7 if 3**3 > 9 else 14
print (a)
# For loop
for i in range(1,10):
    print(i)

for i in range(1,10,2):  #Od 1 do 10 co 2
    print(i)

string = 'String traversal!'
for i in range(len(string)):
    print(string[i])

for char in string:  # Simpler version than above
    print(char)
# 10 x 10 multiplication
for i in range(1,11):
    print ('{:<3}|'.format(i))

# While loop
condition = 10
while condition != 0:
    print (condition)
    condition = condition -1

while True:
    print ("Infinite")
    break

for i in range (1,11):  # Omitting some values
    if i == 5:
        continue
    print(i)

# Functions


def function2():
    print("Tis is our first function!")

function2()


def returning():
    return "I am a result!"

result = returning()
print(result)


def multival():
    return "This is a return value", 2

print (multival())


def parameters(a):
    print (a)
parameters(a="This is a parameter")


def add(y,w):
    c = y + w
    return c

result = add(12,5)
print (result)

resultString = add("One", "String")

print(resultString)


def default_param(a,b=4,c=5):
    return a + b + c
result3 = default_param(3)
print (result3)

# Scope


def scope(z):
    z = z + 1
    print (z)
    return z
scope(5)


def outer(a):

    def nested(b):
        return b * a;
    a = nested(a)
    return a
print (outer(4))


def f(a):
    def g(b):
        def h(c):
            return a * b * c
        return h
    return g
print (f(5)(2)(3))

# Recursive functions which use themselves over and over again


def factorial(n):  # Factorial to Silnia
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)  # 5 * 4 * 3 * 2 * 1
print(factorial(5))


def sums(n):
    if n == 1:
        return 1
    else:
        return n + sums(n - 1)


def tail_sum(n, accumulator=0):
    if n == 0:
        return accumulator
    else:
        return tail_sum(n - 1, accumulator+n)

print (sums(10))
print(tail_sum(10))

# Lambda functions


f = lambda x, y: x + y

print(f(2,3))


j = lambda a: lambda b: lambda c: a * b * c

print(j(3)(2)(4))

k = lambda c: lambda w, x: lambda d: (c * (w + x)) % d

print (k(2)(4, 3)(11))

# Exception handling

try:
    a = 5/0
except Exception as e:
    print (e)

try:
    n = int(input("Enter an integer: "))
except ValueError:
    print("That is not an integer!")

try:
    sumsy = 0
    file = open('numbers.txt', 'r')
    for number in file:
        sumsy = sumsy + 1.0/int(number)
    print(sumsy)
except ZeroDivisionError:
    print ("Number is divided by zero!")
except IOError:
    print ("File DNE")

# Throwing exceptions

a = 'a'


def raiseexception(a):
    if type(a) != type('a'):
        raise ValueError("This is not string")

try:
    raiseexception(a)
except ValueError as e:
    print(e)


def testcase(a, b):
    assert a < b, "a is greater than b"
try:
    testcase(2,1)
except AssertionError as e:
    print(e)

# Data input

age = input ("How old are you?")
print (age)

# File Management  open (filename, access(read or write), buffering)

file = open("C:\\Users\\mkucm\\Desktop\\lol.txt", "r")
print (file.read(4))    # Reads 4 characters from the file
# print (file.tell())     # Cursor is at the fourth position
print (file.seek(6))    # Moves the cursor to the defined position
print(file.tell())
file.close()


file = open("C:\\Users\\mkucm\\Desktop\\lol.txt", "r")
for line in file:
    print(line)  # Writes every line

file.close()

file = open("C:\\Users\\mkucm\\Desktop\\lol.txt", "r")
print ("File Name: " + file.name)
print("is closed: " + str(file.closed))
print("Mode " + file.mode)

# Writing to a file  w+ = writing and reading


file = open("write.txt", "w+")
file.write("Hello file, I am string!")
file.seek(0)
file.write("this")  # overwrites the length of this string from the position of seek function
print(file.read())
file.close()


# Data Structure


tuple = (1, "abc", 2, "cde")
tuple1 = 3, "efg", True
tuple2 = "A"  # tuple2 = ("A",)
print(tuple)