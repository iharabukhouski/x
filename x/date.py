from datetime import datetime
from dateutil.relativedelta import relativedelta

# def process_date(
#     str,
# ):

#     date = datetime.strptime(str, "%m/%d/%y")
#     return date.strftime("%Y-%m-%d")


class date:

    def __init__(
        self,
        date,
    ):

        self.date = date

    @staticmethod
    def range(
        start,
        end,
        years=0,
        months=0,
        days=0,
    ):

        start_date = datetime.now() if start == 'now' else datetime.strptime(start, '%Y-%m-%d')
        end_date = datetime.now() if end == 'now' else datetime.strptime(end, '%Y-%m-%d')

        dates = []

        current_date = start_date

        while current_date >= end_date:

            dates.append(date(current_date))

            current_date += relativedelta(
                years=years,
                months=months,
                days=days,
            )

        return dates

    def format(
        self,
        pattern,
    ):

        patterns = {
            'YYYY': '%Y',
            'MMMM': '%B',
            'MM': '%M',
            'YYYY-MM': '%Y-%m',
        }

        return self.date.strftime(patterns[pattern])
