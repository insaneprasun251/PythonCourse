string = "abcdefghijklmnoprstuvwxyz"

stringList = []
for character in string:
    if character not in ["a", "e", "i", "o", "u"]:
        stringList.append(character)
    else:
        print("Character " + character + " is a vowel")
print(stringList)

sampleText = "Python is a very powerful language"

vowels = frozenset("aeiou")

finalSet = set(sampleText).difference(vowels)
print(finalSet)

finalList = sorted(finalSet)
print(finalList)
