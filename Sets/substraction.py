even = set(range(0, 40, 2))
print(sorted(even))
print(len(even))

squares_tuple = {4, 6, 9, 16, 25}
squares = set(squares_tuple)
print(sorted(squares))

print("even minus squares")
print(even.difference(squares))     # prints even without values that match squares
print("=" * 40)
print(even - squares)

print("--" * 40)
print("squares minus even")
print(squares.difference(even))     # prints squares without values that match even
print("=" * 40)
print(squares - even)

print("=" * 40)
print(sorted(even))
print(squares)
even.difference_update(squares)
print(sorted(even))