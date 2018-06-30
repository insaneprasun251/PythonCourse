nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(any([num % 2 == 0 for num in nums]))  # prints True if any of the elements return True
print(all([num % 2 == 0 for num in nums]))  # prints True if all elements return True

it = ["sds", "gfdgs", "43543"]


def is_string(lst):
    return all(type(i) == str for i in lst)


num = -15.3

print(abs(num))

ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def get_max(lst):
    print(abs(max(lst)))


get_max(ls)

floats = [1, 2.4, 5.5]


def sum_floats(*args):
    print(sum(arg for arg in args if type(arg) == float))


sum_floats(floats)