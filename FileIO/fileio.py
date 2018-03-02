# jabber = open("C:\\Users\\mkucman\\PycharmProjects\\PythonCourse\\FileIO\\sample.txt", 'r')
# jabber = open('sample.txt', 'r')
#
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end='')
#
# jabber.close()

with open("sample.txt", 'r') as jabber:
    for line in jabber:
        if "JAB" in line.upper():
            print(line, end='')

print("=" * 80)

# Now we are removing double lines
with open("sample.txt", 'r') as jabber:
    line = jabber.readline()
    while line:
        print(line, end='')     # end='' means if there is an empty line = don't print it
        line = jabber.readline()

print("=" * 80)

with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines:
    print(line, end='')
