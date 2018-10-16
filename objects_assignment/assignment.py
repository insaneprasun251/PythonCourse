i = 1024
print(hex(i))
print(bin(i))

num = 5.23222
print(round(num, 2))

s = "Hello how are you Mary, are you feeling ok?"


def check_lower(string1):
    for word in string1.split():
        if word[0].isupper():
            return False
        return True


print(check_lower(s))

string2 = "twtwydutwytwyywutwyuwtygwhjwgywguwytwuywgwwwyuwwygwyuw"

print(string2.count('w'))

set1 = {2, 3, 1, 5, 6, 8}
set2 = {3, 1, 7, 5, 6, 8}

print(set1.difference(set2))
print(set1.union(set2))

d = {x: x ** 3 for x in range(5)}

print(d)

list1 = [1, 2, 3, 4]
reversed_list = list(reversed(list1))
print(reversed_list)

list2 = [3, 4, 2, 5, 1]
list_sorted = sorted(list2)
print(list_sorted)
