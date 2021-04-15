import datetime


def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year + 1)]


def current_year():
    return datetime.date.today().year
