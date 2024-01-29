from datetime import datetime


def convert(iso_string: str):
    """
    Convert from an iso-formatted string to a datetime object.
    :param iso_string: str : date_time string
    :return: datetime : the converted date and time
    """
    removed_timezone_str = iso_string[:-1]
    converted_time = datetime.fromisoformat(removed_timezone_str)
    return converted_time
