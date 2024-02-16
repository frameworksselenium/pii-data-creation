import datetime
import random


def ssn():
    # Generate random digits for the SSN
    ssn_digits = [random.randint(0, 9) for _ in range(9)]

    # Ensure that the first digit is between 1 and 9 (to resemble a real SSN)
    ssn_digits[0] = random.randint(1, 9)

    # Add dashes to format the SSN (###-##-####)
    ssn = "{:03d}-{:02d}-{:04d}".format(*ssn_digits)

    return ssn
