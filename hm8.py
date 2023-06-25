from collections import defaultdict
from datetime import date, timedelta, datetime

def get_birthdays_per_week(users):
    today = date.today()
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    days_to_end_of_week = 5 - today.weekday()
    birthdays = {'Past': defaultdict(list), 'This week': defaultdict(list), 'Next week': defaultdict(list)}

    for user in users:
        user_birthday = date(today.year, user['birthday'].month, user['birthday'].day)
        if user_birthday < today:
            category = 'Past'
        elif today <= user_birthday <= today + timedelta(days=days_to_end_of_week):
            category = 'This week'
        else:
            category = 'Next week'

        day_name = weekdays[user_birthday.weekday()] if user_birthday.weekday() < 5 else 'Monday'
        if category == 'Next week' and day_name == 'Monday': 
            day_name = 'Monday'
        birthdays[category][day_name].append(user['name'])

    for category, days in birthdays.items():
        print(f"{category} birthdays:")
        for day, names in days.items():
            if names: 
                print(f'{day}: {", ".join(names)}')

users = [
    {'name': 'Bill', 'birthday': datetime(2023, 6, 1)},
    {'name': 'Jill', 'birthday': datetime(2023, 6, 9)},
    {'name': 'Kim', 'birthday': datetime(2023, 6, 11)},
    {'name': 'Jan', 'birthday': datetime(2023, 6, 14)},
    {'name': 'Lee', 'birthday': datetime(2023, 6, 16)}
]
get_birthdays_per_week(users)
