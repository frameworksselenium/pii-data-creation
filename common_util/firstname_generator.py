import random
import string


def firstname():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=4))
