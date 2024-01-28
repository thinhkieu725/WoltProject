"""
This is the Backend specifics part of the Wolt's trainee assignment.
This project aims to calculate the delivery fee.

The following file(s) must be in the same working directory:
request.json

Creator: Thinh Kieu
Email: thinhkieu726@gmail.com
"""

import json
from datetime import datetime


def read_payload(file_name):
    """
    Get the .json file name and return the content as a dictionary.
    :param file_name: str : name of the file to be read
    :return: dict : the content of the file
    """
    with open("request.json", "r") as file_name:
        content = json.load(file_name)
        return content

def iso_to_datetime(iso_string):
    """
    Convert from an iso-formatted string to a datetime object.
    :param iso_string: str : date_time string
    :return: datetime : the converted date and time
    """
    removed_timezone_str = iso_string[:-1]
    converted_time = datetime.fromisoformat(removed_timezone_str)
    return converted_time


def main():
    # Read the request payload
    request = read_payload("request.json")
    # Convert the iso-formatted time to datetime object
    time_stamp = iso_to_datetime(request["time"])



if __name__ == "__main__":
    main()
