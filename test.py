import unittest

import datetime
from datetime import date
from week import Week, FromFirstDaysWeek

assert Week.thisweek() == Week.create_from_date(datetime.date.today())
week = Week.thisweek()
week.startdate
next_week = week.get_next_week()
next_week.enddate
another_week = week + 1
assert another_week == next_week


class WeekTest(unittest.TestCase):

    def test_year_start_weekday(self):
        for i in range(1, 52):
            self.assertEqual(Week(2019, i).year_start_weekday(), 1)


class FromFirstDaysWeekTest(unittest.TestCase):

    def test_startdate(self):
        self.assertEqual(
            FromFirstDaysWeek(2019, 1).startdate,
            datetime.date(2019, 1, 1))
        self.assertEqual(
            FromFirstDaysWeek(2019, 2).startdate,
            datetime.date(2019, 1, 7))
        self.assertEqual(
            FromFirstDaysWeek(2019, 53).startdate,
            datetime.date(2019, 12, 30))

    def test_enddate(self):
        self.assertEqual(
            FromFirstDaysWeek(2019, 1).enddate,
            datetime.date(2019, 1, 6))
        self.assertEqual(
            FromFirstDaysWeek(2019, 2).enddate,
            datetime.date(2019, 1, 13))
        self.assertEqual(
            FromFirstDaysWeek(2019, 53).enddate,
            datetime.date(2019, 12, 31))

    def test_create_from_date(self):
        self.assertEqual(
            FromFirstDaysWeek.create_from_date(date(2019, 1, 1)),
            FromFirstDaysWeek(2019, 1)
            )
        self.assertEqual(
            FromFirstDaysWeek.create_from_date(date(2019, 1, 6)),
            FromFirstDaysWeek(2019, 1)
            )
        self.assertEqual(
            FromFirstDaysWeek.create_from_date(date(2019, 1, 7)),
            FromFirstDaysWeek(2019, 2)
            )
        self.assertEqual(
            FromFirstDaysWeek.create_from_date(date(2019, 1, 13)),
            FromFirstDaysWeek(2019, 2)
            )
        self.assertEqual(
            FromFirstDaysWeek.create_from_date(date(2019, 12, 29)),
            FromFirstDaysWeek(2019, 52)
            )
        self.assertEqual(
            FromFirstDaysWeek.create_from_date(date(2019, 12, 31)),
            FromFirstDaysWeek(2019, 53)
            )
        self.assertEqual(
            FromFirstDaysWeek.create_from_date(date(2024, 1, 1)),
            FromFirstDaysWeek(2024, 1)
            )
        self.assertEqual(
            FromFirstDaysWeek.create_from_date(date(2024, 1, 7)),
            FromFirstDaysWeek(2024, 1)
            )
        self.assertEqual(
            FromFirstDaysWeek.create_from_date(date(2024, 1, 8)),
            FromFirstDaysWeek(2024, 3)
            )


if __name__ == "__main__":
    unittest.main()
