import datetime

# 1
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
def is_year_leap(year: int) -> bool:
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

now = datetime.datetime.now()
print(f"Today is {WEEKDAYS[now.weekday()]}")
print(f"{now.year} is {"a" if is_year_leap(now.year) else "not a"} leap year")

# 2
def transform_timedelta(delta: datetime.timedelta) -> tuple[int, int, int]:
    days = delta.days
    hours = delta.seconds // 3600
    minutes = delta.seconds % 3600 // 60
    return days, hours, minutes

user_date = datetime.datetime(*(int(n) for n in input("Enter date in 'year-month-day' format: ").split("-")))

if user_date > now:
    delta = user_date - now
    d, h, m = transform_timedelta(delta)
    print(f"{d} days {h} hours {m} minutes left until the entered date")
else:
    delta = now - user_date
    d, h, m = transform_timedelta(delta)
    print(f"The entered date was {d} days {h} hours {m} minutes ago")