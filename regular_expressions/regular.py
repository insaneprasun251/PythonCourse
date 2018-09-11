import re

patterns = ['term1', 'term2']

text = 'This is a string with term1, but not the other term'
result = re.search('hello', 'hello world')
print(result)

for pattern in patterns:
    print('Searching for "%s" in: \n"%s"' % (pattern, text))

    if re.search(pattern, text):
        print('\n')
        print("Match was found. \n")
    else:
        print('\n')
        print("No Match was found. \n")
