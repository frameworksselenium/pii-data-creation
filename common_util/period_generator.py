import datetime


def period():
    # Generate a random month (1 to 12)
    random_month = str(datetime.datetime.now().month)

    # Get the current year
    current_year = str(datetime.datetime.now().year)

    return current_year + '-' + random_month
