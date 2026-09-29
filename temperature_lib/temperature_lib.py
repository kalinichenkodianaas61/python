def is_frost(t):
    """ checks if the temperature is below 0 degrees Celsius """

    return t < 0


def average_temp(temps):
    """ calculates the average temperature from a list of temperatures """

    if len(temps) == 0:
        return None

    total = 0.0
    for t in temps:
        total += t

    return total / len(temps)    


def to_faranheit_all(temps):
    """ converts a list of temperatures from Celsius to  Fahranheit """

    res = []
    for t in temps:
        res.append(t * 9 / 5 + 32) # t(F) = t(C) * 9/5 + 32
    return res


def first_frost(temps):
    """ returns the index of the first frost temperature in a list of temperatures """

    for i in range(len(temps)):
        if is_frost(temps[i]):
            return i
    return -1


def frost_only(temps):
    """ returns a list of frost temperatures from an original list of temperatures """

    res = []
    for t in temps:
        if is_frost(t):
            res.append(t)
    return res