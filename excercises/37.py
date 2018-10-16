def word_counter(file):
    with open(file) as file1:
        file_reader = file1.read()
        str_split = file_reader.replace(',', ' ')
        return len(str_split.split())


print(word_counter('C:\\Users\\mkucman\\Downloads\\words1.txt'))
