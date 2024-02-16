import string
import random


def lastname():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=7))
