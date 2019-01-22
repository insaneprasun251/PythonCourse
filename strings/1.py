string_one = 'python'
string_two = 'planet'

Bulls = 0
Cows = 0

for char_one in string_one:
    for char_two in string_two:
        if char_two in string_one:
            char_two_index = string_two.index(char_two)
            if string_two[char_two_index] == string_one[char_two_index]:
                Bulls += 1
            else:
                Cows += 1

        print("Bulls: " + str(Bulls))
        print("Cows: " + str(Cows))
