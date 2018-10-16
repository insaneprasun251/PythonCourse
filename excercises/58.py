import json

new = {'firstName': "Mat", 'lastName': "Kuc"}
with open('C:\\Users\\mkucman\\Downloads\\company1.json', 'r+') as file:
    x = json.loads(file.read())

    x['employees'].append(new)
    file.seek(0)
    json.dump(x, file, indent=4, sort_keys=True)
    file.truncate()
