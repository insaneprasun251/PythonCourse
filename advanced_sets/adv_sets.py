s = set()
s.add(1)
s.add(2)
print(s)
s.add(3)
s.add(4)
sc = s.copy()
s.add(5)
print(s.difference(sc))
s1 = {1, 2, 3}
s2 = (1, 4, 5)
s1.difference_update(s2)  # Removes from the first set items found in the second set
print(s1)

s3 = {1, 2, 3}
s4 = {1, 2, 4}
s3.intersection_update(s4)  # Sets the items in the set to the matching items in set 4
print(s3)
