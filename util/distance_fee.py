import const
import math


def calculate(delivery_distance: int):
    """
    Calculate the fee caused by delivery distance.
    :param delivery_distance:
    :return:
    """
    # Calculate the delivery fee based on distance
    if delivery_distance <= const.DELI_BASE_DISTANCE:
        distance_fee = const.DELI_BASE_FEE
    else:
        extended_distance = delivery_distance - const.DELI_BASE_DISTANCE
        extended_fee = (
                math.ceil(extended_distance / const.DELI_DISTANCE_INTERVAL)
                * const.DELI_FEE_PER_INTERVAL)
        distance_fee = const.DELI_BASE_FEE + extended_fee

    return distance_fee
