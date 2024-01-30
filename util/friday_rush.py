from util import iso_to_datetime
import const


def check(time: str):
    """
    Check whether the given time is in the Friday rush hours.
    :param time: str: The time in ISO 8601 format
    :return: bool: True if the time is within Friday rush hours
    """
    # Convert the time to datetime object
    time_stamp = iso_to_datetime.convert(time)

    # Check if Friday rush fee applies
    if time_stamp.isoweekday() == const.FRIDAY_IDX:
        hour = time_stamp.hour
        if const.RUSH_HOUR_START <= hour < const.RUSH_HOUR_END:
            return True

    return False
