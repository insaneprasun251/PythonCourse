file = open("write.txt", "w+")
file.write("Hello file, I am string!")
file.seek(0)
file.write("this")  # overwrites the length of this string from the position of seek function
print(file.read())
file.close()