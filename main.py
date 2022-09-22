from datetime import datetime
from collections import defaultdict


def get_birthdays_per_week(users: list) -> None:
    """
    Simple function, that receive list of users and print name and day of birth
    for upcoming 7 days.
    :param users: is a list of dicts where there are pairs ('name': 'string')
    and ('birthday': datetime object)
    """
    birth_dict = defaultdict(str)
    for person in users:
        day_dif = (person['birthday'] - datetime.now())
        if day_dif.days <= 7:
            day = datetime.strftime(person['birthday'], '%A')
            if (day == 'Saturday') or (day == 'Sunday'):
                day = 'Monday'
            birth_dict[f'{day}'] += (person['name']) + ', '
    for key in birth_dict:
        if birth_dict[key].endswith(', '):
            birth_dict[key] = birth_dict[key][0:-2]
        print(key, ': ', birth_dict[key])


if __name__ == '__main__':
    users_ = [
        {'name': 'Jim', 'birthday': datetime(2022, 9, 23)},
        {'name': 'Anna', 'birthday': datetime(2022, 9, 24)},
        {'name': 'Perry', 'birthday': datetime(2022, 9, 24)},
        {'name': 'Mike', 'birthday': datetime(2022, 9, 25)},
        {'name': 'Robin', 'birthday': datetime(2022, 9, 26)},
        {'name': 'Vika', 'birthday': datetime(2022, 9, 26)},
        {'name': 'Miranda', 'birthday': datetime(2022, 9, 27)},
        {'name': 'Robin', 'birthday': datetime(2022, 9, 28)},
        {'name': 'Vika', 'birthday': datetime(2022, 9, 28)},
        {'name': 'Miranda', 'birthday': datetime(2022, 10, 1)}
    ]

    get_birthdays_per_week(users_)
