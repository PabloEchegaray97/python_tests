## dates ##

from datetime import datetime
from datetime import date
now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
#formato posix
timestamp = now.timestamp() #representacion unica de un tiempo
print(timestamp)

year_2023 = datetime(2023,1,1)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.timestamp())

print_date(year_2023)

