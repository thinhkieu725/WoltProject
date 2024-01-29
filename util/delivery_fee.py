import math

import const
from util import surcharges, friday_rush, distance_fee


def calculate(cart_value: int, delivery_distance: int,
              number_of_items: int, time: str):
    """
    Calculate the delivery fee for the order with given parameters.
    :param cart_value: int : total value of the cart (in cents)
    :param delivery_distance: int : delivery distance (in meters)
    :param number_of_items: int : number of item
    :param time: string : time stamp of the order in ISO format
    :return: int : delivery fee (in cents)
    """
    # Free delivery for 200e or over cart
    if cart_value >= const.FREE_DELI_CART_VALUE:
        return 0

    # Calculate the dee caused by delivery distance
    dist_fee = distance_fee.calculate(delivery_distance)

    # Calculate the surcharges
    total_surcharge = surcharges.calculate(cart_value, number_of_items)

    # Calculate the delivery fee including surcharges
    delivery_fee = dist_fee + total_surcharge

    # Calculate the delivery fee after considering Friday rush hours
    if friday_rush.check(time):
        delivery_fee *= const.FRI_RUSH_RATE
        delivery_fee = int(delivery_fee)

    # Limit the maximum delivery fee
    if delivery_fee > const.MAX_DELI_FEE:
        delivery_fee = const.MAX_DELI_FEE

    return delivery_fee
