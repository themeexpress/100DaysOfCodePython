"""This is how you work out whether if a particular year is a leap year.

on every year that is divisible by 4 with no remainder

except every year that is evenly divisible by 100 with no remainder

unless the year is also divisible by 400 with no remainder
explain it with example
"""

def is_leap_year(year: int) -> bool:
    """
    Check if a year is a leap year.

    Parameters
    ----------
    year : int
        The year to check.

    Returns
    -------
    bool
        True if the year is a leap year, False otherwise.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(is_leap_year(2000))  # True, because 2000 is divisible
print(is_leap_year(1900))  # False, because 1900 is divisible by 100 but not by 400
print(is_leap_year(2020))  # True, because 2020 is divisible by 4 but not by 100
print(is_leap_year(2021))  # False, because 2021 is not divisible by 4
print(is_leap_year(1600))  # True, because 1600 is divisible by 400