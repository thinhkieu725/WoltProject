"""
This is the Backend specifics part of the Wolt's trainee assignment.
This project aims to calculate the delivery fee.

The request*.json file(s) must be in the same working directory with this file.

Creator: Thinh Kieu
Email: thinhkieu726@gmail.com
"""

from datetime import datetime
import math
from fastapi import FastAPI, Body, HTTPException
from util import delivery_fee, input_validation

# API creating and processing
app = FastAPI()


@app.post("/delivery_fee_calculator")
async def delivery_fee_response(
        cart_value: int = Body(...),
        delivery_distance: int = Body(...),
        number_of_items: int = Body(...),
        time: str = Body(...),
):
    # Check whether inputs are valid
    err_code, description = input_validation.check(
        cart_value, delivery_distance, number_of_items, time)
    if err_code is not None:
        raise HTTPException(status_code=422, detail=description)

    # Calculate the delivery fee
    total_delivery_fee = delivery_fee.calculate(
        cart_value, delivery_distance,number_of_items, time)
    # Create response payload
    response_data = {"delivery_fee": total_delivery_fee}

    return response_data

