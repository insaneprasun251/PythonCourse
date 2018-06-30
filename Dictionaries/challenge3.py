def multiple_letter_count(word):
    dict = {}
    for letter in word:
        dict[letter] += 1
    print(dict)
    return dict

def multiply_even_numbers(aList):
    total = 0
    for number in aList:
        if number % 2 == 0:
            if total == 0:
                total += number
            else:
                total *= number
    print(total)
    return total

def capitalize(string):
    capitalized = string[0].upper() + string[1::]
    print(capitalized)
    return capitalized

if __name__ == '__main__':
    capitalize("tim")
