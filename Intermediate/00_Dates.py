## dates ##

from datetime import datetime
from datetime import time
from datetime import date
from datetime import timedelta

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


##################################
#objeto que permite encapsular tiempo
current_time = time(21,6,0)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

##################################
#objeto que permite encapsular fecha
current_date = date(2030,4,25)
current_date = date.today()
print(current_date.year)
print(current_date.month)
print(current_date.day)
current_date = date(current_date.year, current_date.month, current_date.day+1) # de esta forma si podemos editarlo
print(current_date.day)

diff = now - year_2023
print(diff)
diff = current_date - year_2023.date()
print(diff)
##################################
#operar y trabajar con fechas
start_time_delta = timedelta(200, 100, 100, weeks=10, hours=20)
end_time_delta = timedelta(300, 100, 100, weeks=13)
print(end_time_delta - start_time_delta)
print(end_time_delta / start_time_delta)
