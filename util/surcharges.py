import const


def calculate(cart_value: int, number_of_items: int):
    """
    This function calculate the surcharges, including small order surcharge,
    large number of item surcharge and the bulk fee for an order of over 12
    items.
    :param cart_value: int : total value of the cart (in cents)
    :param number_of_items: int : number of item
    :return: int : the total surcharge
    """
    # Establish a dict to store surcharges
    surcharges = {"small_order": 0, "large_num_items": 0, "bulk": 0}

    # Calculate small order surcharge
    if cart_value < const.MIN_FREECHARGE_CART_VALUE:
        surcharges[
            "small_order"] = const.MIN_FREECHARGE_CART_VALUE - cart_value

    # Calculate large number of items surcharge and bulk fee
    if number_of_items > const.MAX_FREECHARGE_NUM_ITEMS:
        charged_items = number_of_items - const.MAX_FREECHARGE_NUM_ITEMS
        surcharges[
            "large_num_items"] = charged_items * const.FEE_PER_EXCESS_ITEM
        if number_of_items > const.MAX_NO_BULKFEE_NUM_ITEMS:
            surcharges["bulk"] = const.BULK_FEE

    return sum(surcharges.values())