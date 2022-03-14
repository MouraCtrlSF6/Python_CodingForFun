import datetime

def has_friday_13th(month, year):
    d = datetime.date(year, month, 13)   
    return d.isoweekday() == 5

month = int(input("Type a month: "))
year = int(input("Type a year: "))

if has_friday_13th(month, year):
    print("Yes, it has a friday 13th")
else: 
    print("No, it doesn't have a friday 13th")