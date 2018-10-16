def file_splitter(file_path):
    with open(file_path) as file1:
        file_split = file1.read()
        str_list = file_split.split()
        return len(str_list)


print(file_splitter('C:\\Users\\mkucman\\Downloads\\words1.txt'))
