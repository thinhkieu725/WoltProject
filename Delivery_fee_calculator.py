"""
This is the Backend specifics part of the Wolt's trainee assignment.
This project aims to calculate the delivery fee.

The following file(s) must be in the same working directory:
request.json

Creator: Thinh Kieu
Email: thinhkieu726@gmail.com
"""

import json


def read_payload(file_name):
    """
    Get the .json file name and return the content as a dictionary.
    :param file_name: str : name of the file to be read
    :return: dict : the content of the file
    """
    with open("request.json", "r") as file_name:
        content = json.load(file_name)
        return content


def main():
    # Read the request payload
    request = read_payload("request.json")


if __name__ == "__main__":
    main()
