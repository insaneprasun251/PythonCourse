even = set(range(0, 40, 2))
print(even)
print(len(even))

square_tuple = {4, 6, 9, 16, 25}
squares = set(square_tuple)
print(len(squares))

print(even.union(squares))  # adds the squares to the even set, but only unique ones
print(len(even.union(squares)))

print("-" * 40)

print(even.intersection(squares))   # looks for the matching values between sets
print(even & squares)
print(squares.intersection(even))
print(squares & even)

