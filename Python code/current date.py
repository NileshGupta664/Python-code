"""from datetime import date
today_date=date.today()
print("current year is",today_date.year)
print("current month is",today_date.month)
print("current date is",today_date.day)"""
from datetime import date, datetime
now=datetime.now()
print("current date and time is:",now)
c_time=now.strftime("%H:%M:%S")
print("current time=",c_time)