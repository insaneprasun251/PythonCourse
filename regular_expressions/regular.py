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

match = re.search(patterns[0], text)
print(type(match))

print(match.start())

split_term = '@'

phrase = 'What is your email, is it hello@gmail.com?'

print(re.split(split_term, phrase))

print(re.findall('match', 'Here is one match, here is another match'))


def multi_re_find(patterns_list, phrase_text):
    """

    :param patterns_list: List of regex patterns
    :param phrase_text: Text against which we are finding matches
    :return: Prints a list of all matches
    """
    for pat in patterns_list:
        print("Searching the phrase using the re check: %r" % pat)
        print(re.findall(pat, phrase_text))
        print('\n')


test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = ['sd*',  # s followed by zero or more d's
                 'sd+',  # s followed by one or more d's
                 'sd?',  # s followed by zero or one d's
                 'sd{3}',  # s followed by three d's
                 'sd{2,3}'  # s followed by two to three d's
                 ]

multi_re_find(test_patterns, test_phrase)

test_patterns_two = ['[sd]',  # either s or d
                     's[sd]+'  # s followed by one or more s or d
                     ]

multi_re_find(test_patterns_two, test_phrase)

test_phrase_two = 'This is a string! But it has punctuation. How can I remove it?'
print(re.findall('[^!.? ]+', test_phrase_two))

test_phrase_three = 'THIS is an example sentence. Let\'s see if we can find some letters.'

test_patterns_three = ['[a-z]+',  # sequences of lower case characters
                       '[A-Z]+',  # sequences of upper case characters
                       '[a-zA-Z]+',  # sequences of lower or upper case letters
                       '[A-Z][a-z]+'  # one upper case letter followed by lower case letters
                       ]

multi_re_find(test_patterns_three, test_phrase_three)

escape_codes = ['\d',  # digit
                '\D',  # a non-digit
                '\s',  # whitespace (tab, space, newline etc.)
                '\S',  # non-whitespace
                '\w',  # alphanumeric
                '\W'  # non-alphanumeric
                ]

escape_codes_phrase = 'THIS is an example sentence! Let\'s see if we can find some letters.' \
                      ' 1 is a hero, 2 is a sheep, 34 is cow.'

multi_re_find(escape_codes, escape_codes_phrase)

test_phrase_four = 'This is a string with some numbers 1233 and a symbol #hashtag'
test_patterns_four = [r'\d+',  # sequence of digits
                      r'\D+',  # sequence of non-digits
                      r'\s+',  # sequence of whitespace
                      r'\S+',  # sequence of non-whitespace
                      r'\w+',  # sequence of alphanumeric characters
                      r'\W+'  # sequence of non-alphanumeric characters
                      ]

multi_re_find(test_patterns_four, test_phrase_four)
