import random
import datetime


def dob(start_year=1990, end_year=(datetime.date.today().year-5)):
    # Generate a random year within the specified range
    random_year = random.randint(start_year, end_year)

    # Generate a random month (1 to 12)
    random_month = random.randint(1, 12)

    # Generate a random day within the range of the selected month and year
    if random_month in [1, 3, 5, 7, 8, 10, 12]:
        random_day = random.randint(1, 31)
    elif random_month in [4, 6, 9, 11]:
        random_day = random.randint(1, 30)
    else:  # February
        if random_year % 4 == 0 and (random_year % 100 != 0 or random_year % 400 == 0):  # Leap year
            random_day = random.randint(1, 29)
        else:
            random_day = random.randint(1, 28)

    # Create a datetime object representing the random DOB
    random_dob = datetime.date(random_year, random_month, random_day)

    return random_dob
