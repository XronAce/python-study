import datetime as dt

now = dt.datetime.now()
for day in range(5, 0, -1):
    print(now - dt.timedelta(days = day))