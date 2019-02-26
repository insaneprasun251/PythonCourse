class StringManipulation:
    def __init__(self):
        self.s = ''

    def get_string(self):
        self.s = input("Input text: ")

    def print_string(self):
        print(self.s.upper())


if __name__ == '__main__':
    string1 = StringManipulation()
    string1.get_string()
    string1.print_string()
