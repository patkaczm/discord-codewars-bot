from codewars import CodewarsAPI, CodewarsTasks
from datetime import timedelta


class Round:
    class StartTimeErrorException(Exception):
        def __init__(self):
            super().__init__("Round can be started only on Monday")

    class Dates:
        def __init__(self, start_date, end_date):
            self.start_date = start_date
            self.end_date = end_date

    def __init__(self, start_date):
        if start_date.weekday() != 0:
            raise self.StartTimeErrorException()
        self.start_date = start_date.replace(hour=0, minute=00, second=00)

        self.end_date = self.start_date + timedelta(weeks=1, seconds=-1)

    def get_dates(self):
        return self.Dates(self.start_date, self.end_date)
