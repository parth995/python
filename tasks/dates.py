import datetime

tday = datetime.date.today()

print(tday)
print(tday.weekday())

tdelta = datetime.timedelta(days=7)

bday = datetime.date(1997, 5, 17)

till_bday = bday - tday

print(abs(till_bday.days))