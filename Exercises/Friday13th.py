import datetime
def has_friday_13th(month, year):
    d = datetime.date(year, month, 13)   
    if d.isoweekday() == 5:
        return True
    else: return False

month = int(input("Type a month: "))
year = int(input("Type a year: "))
call_back = has_friday_13th(month, year)
if call_back:
    print("Yes, it has a friday 13th")
else: print("No, it doesn't have a friday 13th")