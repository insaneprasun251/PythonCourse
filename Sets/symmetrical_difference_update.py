even = set(range(0, 40, 2))
print(sorted(even))
squares_tuple = {4, 6, 9, 16, 25}
squares = set(squares_tuple)
print(sorted(squares))

# squares.discard(4)
# squares.remove(16)
# squares.discard(8)      # no error, does nothing
# print(squares)
# try:
#     squares.remove(8)       # error for remove function when element is not there
# except KeyError:
#     print("The item 8 is not a member of the set")

even = set(range(0, 40, 2))
print(even)
squares_tuple = (4, 6, 16)
squares = (set(squares_tuple))
print(squares)

if squares.issubset(even):
    print("squares is a subset of even")        # squares are part of even

if even.issuperset(squares):
    print("even is a superset of squares")      # even contains all of the values from squares

