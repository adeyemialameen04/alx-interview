#!/usr/bin/python3
"""Documenting modules"""


def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the most significant bits
    mask1 = 1 << 7  # 10000000 in binary
    mask2 = 1 << 6  # 01000000 in binary

    for byte in data:
        # Get the last 8 bits of the integer
        byte = byte & 0xFF

        if num_bytes == 0:
            # Count the number of leading 1's
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            # 1 byte character
            if num_bytes == 0:
                continue

            # Invalid scenarios for UTF-8
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrease the number of bytes to process for the current character
        num_bytes -= 1

    # If we have processed all expected bytes
    return num_bytes == 0
