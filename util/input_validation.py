from datetime import datetime


def check(
        cart_value: int,
        delivery_distance: int,
        number_of_items: int,
        time: str):
    error_code = None
    details = ""

    # Check whether there is any parameter missing.
    if (cart_value is None or delivery_distance is None or
            number_of_items is None or time is None):
        error_code = 422
        details = "One or more required parameters are missing."
        return error_code, details

    # Check whether parameters are of their correct type
    if not isinstance(cart_value, int):
        error_code = 422
        details = "The cart value must be an integer."
        return error_code, details

    if not isinstance(delivery_distance, int):
        error_code = 422
        details = "The delivery distance must be an integer."
        return error_code, details

    if not isinstance(number_of_items, int):
        error_code = 422
        details = "The number of items must be an integer."
        return error_code, details

    if not isinstance(time, str):
        error_code = 422
        details = "The time parameter must be a string."
        return error_code, details

    # Check whether the integers value are positive
    if cart_value < 0:
        error_code = 422
        details = "The cart value must not be negative."
        return error_code, details

    if delivery_distance <= 0:
        error_code = 422
        details = "The delivery distance must be greater than 0."
        return error_code, details

    if number_of_items <= 0:
        error_code = 422
        details = "The number of items must be greater than 0."
        return error_code, details

    if not is_iso_format(time):
        error_code = 422
        details = "The time must be in ISO 8601 format."
        return error_code, details

    return error_code, details


def is_iso_format(input_string):
    try:
        # Try to parse the string as ISO format
        datetime.strptime(input_string, "%Y-%m-%dT%H:%M:%SZ")
        return True
    except ValueError:
        return False
