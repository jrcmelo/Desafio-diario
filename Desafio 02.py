import datetime

time = input(datetime.time)

date_time = datetime.datetime.strptime(time, "%H:%M:%S")
a_timedelta = date_time - datetime.datetime(1900, 1, 1)
seconds = a_timedelta.total_seconds()

print(seconds)