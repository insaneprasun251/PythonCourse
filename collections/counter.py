from collections import Counter

l = [1, 1, 1, 1, 1, 12, 2, 2, 2, 2, 2, 4, 4, 3, 4, 4, 34, 34, 433, 3, 33, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, ]

print(Counter(l))

s = "Multiplication of those number results in the provided number :"
words = s.split()
c = Counter(words)
print(c.most_common(2))
