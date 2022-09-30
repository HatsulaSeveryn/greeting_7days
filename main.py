from datetime import datetime, timedelta


def get_birthdays_per_week(users: list) -> None:
    """
    Simple function, that receive list of users and print name and day of birth
    for upcoming 7 days.
    :param users: is a list of dicts where there are pairs ('name': 'string')
    and ('birthday': datetime object)
    """
    birth_days = {}
    for ind_ in range(7):
        birth_days[datetime.strftime(datetime.now() + timedelta(days=ind_), '%A')] = []
    for person in users:
        year_ = datetime.now().year
        day_dif = (datetime.now() - person['birthday'].replace(year=year_))
        if 0 <= day_dif.days <= 7:
            day = datetime.strftime(person['birthday'], '%A')
            if day in ('Saturday', 'Sunday'):
                day = 'Monday'
            birth_days[f'{day}'].append(person['name'])
    for b_day in birth_days:
        if birth_days[b_day]:
            print(b_day, ': ', ', '.join(birth_days[b_day]))


if __name__ == '__main__':
    users_ = [
        {'name': 'Jim', 'birthday': datetime(1975, 10, 23)},
        {'name': 'Miranda', 'birthday': datetime(2010, 10, 27)},
        {'name': 'Robin', 'birthday': datetime(2001, 9, 28)},
        {'name': 'Vika', 'birthday': datetime(2005, 9, 28)},
        {'name': 'Miranda', 'birthday': datetime(2003, 10, 1)},
        {'name': 'Anna', 'birthday': datetime(2002, 9, 24)},
        {'name': 'Perry', 'birthday': datetime(1985, 9, 24)},
        {'name': 'Mike', 'birthday': datetime(1999, 9, 25)},
        {'name': 'Robin', 'birthday': datetime(1980, 10, 26)},
        {'name': 'Vika', 'birthday': datetime(2000, 9, 26)}
    ]

    get_birthdays_per_week(users_)
