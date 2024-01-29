"""
This is the Backend specifics part of the Wolt's trainee assignment.
This project aims to calculate the delivery fee.

The request*.json file(s) must be in the same working directory with this file.

Creator: Thinh Kieu
Email: thinhkieu726@gmail.com
"""

from datetime import datetime
import math
from fastapi import FastAPI, Body

# Constants for delivery fee calculation
FREE_DELI_CART_VALUE = 20000

MIN_FREECHARGE_CART_VALUE = 1000

DELI_BASE_DISTANCE = 1000
DELI_BASE_FEE = 200
DELI_DISTANCE_INTERVAL = 500
DELI_FEE_PER_INTERVAL = 100

MAX_FREECHARGE_NUM_ITEMS = 4
FEE_PER_EXCESS_ITEM = 50
MAX_NO_BULKFEE_NUM_ITEMS = 12
BULK_FEE = 120

FRI_RUSH_RATE = 1.2
FRIDAY_IDX = 5  # System constant
RUSH_HOUR_START = 15
RUSH_HOUR_END = 19

MAX_DELI_FEE = 1500

# Constant for testing and operating
REQUEST_FILE = "request1.json"
RESPONSE_FILE = "response1.json"

# API creating and processing
app = FastAPI()


@app.post("/delivery_fee_calculator")
async def delivery_fee_response(
    cart_value: int = Body(...),
    delivery_distance: int = Body(...),
    number_of_items: int = Body(...),
    time: str = Body(...),
):
    # Calculate the delivery fee
    delivery_fee = calculate_delivery_fee(cart_value, delivery_distance,
                                          number_of_items, time)
    # Create response payload
    response_data = {"delivery_fee": delivery_fee}

    return response_data


def iso_to_datetime(iso_string: str):
    """
    Convert from an iso-formatted string to a datetime object.
    :param iso_string: str : date_time string
    :return: datetime : the converted date and time
    """
    removed_timezone_str = iso_string[:-1]
    converted_time = datetime.fromisoformat(removed_timezone_str)
    return converted_time


def calculate_delivery_fee(cart_value: int, delivery_distance: int,
                           number_of_items: int, time: int):
    """
    Calculate the delivery fee for the order with given parameters.
    :param cart_value: int : total value of the cart (in cents)
    :param delivery_distance: int : delivery distance (in meters)
    :param number_of_items: int : number of item
    :param time: string : time stamp of the order in ISO format
    :return: int : delivery fee (in cents)
    """
    # Free delivery for 200e or over cart
    if cart_value >= FREE_DELI_CART_VALUE:
        return 0

    # Convert the time to datetime object
    time_stamp = iso_to_datetime(time)

    # Establish a dict to store surcharges
    surcharges = {"small_order": 0, "large_num_items": 0, "bulk": 0}

    # Calculate small order surcharge
    if cart_value < MIN_FREECHARGE_CART_VALUE:
        surcharges["small_order"] = MIN_FREECHARGE_CART_VALUE - cart_value

    # Calculate the delivery fee based on distance
    delivery_fee = 0
    if delivery_distance <= DELI_BASE_DISTANCE:
        delivery_fee = DELI_BASE_FEE
    else:
        extended_distance = delivery_distance - DELI_BASE_DISTANCE
        extended_fee = (math.ceil(extended_distance / DELI_DISTANCE_INTERVAL)
                        * DELI_FEE_PER_INTERVAL)
        delivery_fee = DELI_BASE_FEE + extended_fee

    # Calculate large number of items surcharge and bulk fee
    if number_of_items > MAX_FREECHARGE_NUM_ITEMS:
        charged_items = number_of_items - MAX_FREECHARGE_NUM_ITEMS
        surcharges["large_num_items"] = charged_items * FEE_PER_EXCESS_ITEM
        if number_of_items > MAX_NO_BULKFEE_NUM_ITEMS:
            surcharges["bulk"] = BULK_FEE

    # Calculate the delivery fee including surcharges
    delivery_fee += sum(surcharges.values())

    # Check if Friday rush fee applies
    if time_stamp.isoweekday() == FRIDAY_IDX:
        hour = time_stamp.hour
        if RUSH_HOUR_START <= hour < RUSH_HOUR_END:
            delivery_fee *= FRI_RUSH_RATE
            delivery_fee = int(delivery_fee)

    # Limit the maximum delivery fee
    if delivery_fee > MAX_DELI_FEE:
        delivery_fee = MAX_DELI_FEE

    return delivery_fee
