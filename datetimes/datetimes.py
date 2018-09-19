import datetime

t = datetime.time(5, 25, 1)

print(t)
print(t.tzinfo)

today = datetime.date.today()

print(today)

d1 = datetime.date(2018, 3, 11)

d2 = d1.replace(year=2000)

print(d2)
print(d1 - d2)
