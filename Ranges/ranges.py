# my_list = list(range(10))
#
# even = list(range(0, 1000, 2))
# odd = list(range(1, 1000, 2))
# print(my_list)
# print(even)
# print(odd)
# my_string = "abcdefghijklmnoprstuvwxzyz"
# print(my_string.index('e'))
#
# print(my_string[4])
#
# small_decimals = range(0, 10)
# print(small_decimals)
# print(small_decimals.index(3))
#
# odd = range(1, 10000, 2)
# print(odd)
#
# print(odd[985])
#
# sevens = range(7, 100000, 7)
#
# x = int(input("Please enter a positive number less than a million: "))
#
# if x in sevens:
#     print("{} is divisible by seven".format(x))
# else:
#     print("{} is not divisible by seven".format(x))
#
# print(small_decimals)
# my_range = small_decimals[::2]
# print(my_range)
# # Searches for index of the element 4, not for the element at index 4
# print(my_range.index(4))

# decimals = range(0, 100)
# my_range = decimals[3:40:3]
# print(my_range == range(3, 40, 3))

my_range = range(0, 100, 4)
print(my_range)
for i in my_range[::-1]:
    print(i)
print("=" * 50)
cut = my_range[3:80:4]
for i in cut:
    print(i)



