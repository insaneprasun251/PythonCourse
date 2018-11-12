checklist = ["Portugal", "Spain", "Germany"]

with open('countries_missing.txt', 'r') as file:
    countries = file.readlines()
added_countries = countries
for i in checklist:
    added_countries.append(i + "\n")

print(sorted(added_countries))

with open('countries_added', 'w') as file:
    file.writelines(sorted(added_countries))
