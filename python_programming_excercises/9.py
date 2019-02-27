# 10

"""
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all
duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use set container to remove duplicated data automatically and then use sorted() to sort the data.

"""
input_text = input("Provide input text: ")
input_list = []
for element in input_text.split():
    if element in input_list:
        continue
    else:
        input_list.append(element)

print(sorted(input_list))