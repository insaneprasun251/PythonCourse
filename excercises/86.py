checklist = ["Portugal", "Germany", "Munster", "Spain"]

with open('countries_clean.txt', 'r') as file:
    content = file.readlines()
    content_list = [i.strip("\n") for i in content if "\n" in i]

cleaned_checklist = [i for i in checklist if i in content_list]
print(cleaned_checklist)
