from datetime import datetime

from collections import defaultdict

weekdays_dict = {
    0: 'Monday', 1: 'Tuesday', 2: 'Wednesday',
    3: 'Thursday', 4: 'Friday', 5: 'Saturday',
    6: 'Sunday', 7: 'Monday Next Week'
}

users = [
    {"name": "John Smith", "birthday": datetime(2015, 2, 25)},
    {"name": "Iren Rose", "birthday": datetime(1967, 2, 20)},
    {"name": "Serg Gibarian", "birthday": datetime(1999, 2, 24)},
    {"name": "Robert Sortorius", "birthday": datetime(2003, 2, 25)},
    {"name": "Dmitro Petrik", "birthday": datetime(2010, 2, 19)},
    {"name": "Bill First", "birthday": datetime(1981, 2, 21)},
    {"name": "Will Second", "birthday": datetime(1981, 12, 13)},
    {"name": "Roger Wathers", "birthday": datetime(1993, 5, 29)}
]


def get_birthdays_per_week(users):
    birthday_list = []
    birthday_sorted = []
    today = datetime.today().date()
    schedule = defaultdict(list)
    title = ''

    def create_birthday_list():
        for user in users:
            name = user["name"]
            birthday = user["birthday"].date()
            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday.replace(year=today.year+1)
            delta_days = (birthday_this_year - today).days

            if delta_days < 7:
                birthday_list.append({birthday_this_year.weekday(): [name]})

    def sorted_birthday_list(birthdays):
        nonlocal birthday_sorted
        birthday_dict = {}

        for weekday in birthdays:
            for key, value in dict(weekday).items():
                if key in birthday_dict.keys():
                    temp = ''
                    temp = birthday_dict[key]
                    temp += value
                    birthday_dict[key] = temp
                    break

                birthday_dict[key] = value

        birthday_sorted = sorted(birthday_dict.items())
        return birthday_sorted

    def create_schedule():
        weekend = []

        for key, value in birthday_sorted:
            if key >= 5:
                weekend += value
            else:
                schedule[weekdays_dict[key]] = value

        schedule[weekdays_dict[7]] = weekend

    def printing_list():
        nonlocal title
        for key, value in schedule.items():
            title += key+':'+', '.join(value)+'\n'
        title = title.removesuffix('\n')

    create_birthday_list()
    sorted_birthday_list(birthday_list)
    create_schedule()
    printing_list()

    return title


print(get_birthdays_per_week(users))
