even = set(range(0, 40, 2))
print(sorted(even))
squares_tuple = {4, 6, 9, 16, 25}
squares = set(squares_tuple)
print(sorted(squares))

print("symmetric even minus squares")
print(sorted(even.symmetric_difference(squares)))

print("symmetric squares minus even")
print(squares.symmetric_difference(even))