#!/usr/bin/python3
"""Determines if a given data set represents a valid UTF-8 encoding."""


def validUTF8(data):
    """
    Return if data passed is a valit UTF-8 encoding.

    It checks whether each byte follows the correct format.
    if the correct number of continuation bytes exist.
    """
    byte_number = 0

    # checks for continuation bytes format 10******
    one_byte = 1 << 7
    two_byte = 1 << 6

    for byte in data:
        # incrementing check to determine if it's a multi-byte character
        mask = 1 << 7
        if byte_number == 0:
            while mask & byte:
                byte_number += 1
                mask >>= 1

            if byte_number == 0:
                continue

            if byte_number == 1 or byte_number > 4:
                return False
        else:
            if not (byte & one_byte and not (byte & two_byte)):
                return False

        byte_number -= 1
    return byte_number == 0
