import string

with open('./write.txt', 'w') as file1:
    for i in string.ascii_lowercase:
        file1.write(i + '\n')
