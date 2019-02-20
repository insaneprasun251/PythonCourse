list_of_ints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
result = list(filter(lambda x: x % 2 == 0, list_of_ints))

print(result)
