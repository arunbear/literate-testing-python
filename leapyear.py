def is_leap_year(year):
    if year <= 0:
        raise ValueError()
    if (year % 4 == 0) and (year % 100 != 0):
        return True
    elif year % 400 == 0:
        return True
    else:
        return False
