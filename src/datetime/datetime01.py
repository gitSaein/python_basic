import datetime

now = datetime.datetime.now()

year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second

print("{}년 {}월 {}일 {}시 {}분 {}초".format(year, month, day, hour, minute, second))

if hour < 12:
    print("현재 시각은 {}:{} \'오전\' 입니다.".format(hour, minute))
if hour >= 12:
    print("현재 시각은 {}:{} \'오후\' 입니다.".format(hour, minute))
