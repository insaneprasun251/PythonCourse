from collections import defaultdict, OrderedDict

d = {'k1': 1}
print(d['k1'])

d = defaultdict(object)
d['one']
for item in d:
    print(item)

d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

for k, v in d.items():
    print(k, v)

d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

for k, v in d.items():
    print(k, v)
