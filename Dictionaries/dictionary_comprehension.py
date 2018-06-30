# list1 = ["CA", "NJ", "RI"]
# list2 = ["California", "New Jersey", "Rhode Island"]
#
# # make sure your solution is assigned to the answer variable so the tests can work!
# answer = dict(zip(list1, list2))
# print(answer)
#

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer = {}
for item in person:
    answer[item[0]] = item[1]

print(answer)