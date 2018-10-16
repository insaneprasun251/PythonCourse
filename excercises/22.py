d = {'a': list(range(1, 11)), 'b': list(range(11, 21)), 'c': list(range(21, 31))}
print(d)
print(d['b'][2])
for key in d.keys():
    print(key + ' has value ' + str(d[key]))

