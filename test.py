import datetime
from week import Week
assert Week.thisweek() == Week.create_from_date(datetime.date.today())
week = Week.thisweek()
week.startdate
next_week = week.get_next_week()
next_week.enddate
another_week = week + 1
assert another_week == next_week
print(Week.create_from_date(datetime.date(2017,1,1)))
print(Week.create_from_date(datetime.date(2017,1,10)))
