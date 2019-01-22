# 1
data = [str(x) for x in open("checksum.txt").readlines()]
c = [0, 0]
for line in data:
    found_two = False
    found_three = False
    for i in line:
        count = line.count(i)
        if not found_two and count == 2:
            c[0] += 1
            found_two = True
        elif not found_three and count == 3:
            c[1] += 1
            found_three = True
        if found_two and found_three:
            break
print(c[0] * c[1])

# 2
for line in data:
    for letter in line:
        # TODO: everything
        print("Hi")
