#!/usr/bin/python3
"""
a python module to validate the utf-8 encoding
"""


def validUTF8(data):
    """
    validateUTF8 - a python function to validate utf-8 encoding
        the rules
        1. For a 1-byte character, the first bit is a 0, followed by its
           Unicode code.
        2. For an n-bytes character, the first n bits are all one's,
           the n + 1 bit is 0, followed by n - 1 bytes with the most
           significant 2 bits being 10.
    Arguments:
        data: the given data to check
    Returns:
        true if the data is a valide utf8 else 0
    """
    ln = len(data)
    i = 0
    """ iterate each number"""
    while i < ln:
        num = data[i]
        bytes_nbr = 0
        """ determine the number of bytes just mask with some number to find
        the most significat digits
        """
        if num >= 255:
            return False
        if num & 128 == 0:
            bytes_nbr = 1
        elif num & 224 == 192:
            bytes_nbr = 2
        elif num & 240 == 224:
            bytes_nbr = 3
        elif num & 248 == 240:
            bytes_nbr = 4
        else:
            return False

        for j in range(1, bytes_nbr, 1):
            if (j + i >= ln):
                return False
            nxt_nbr = data[j + i]
            if (nxt_nbr & 192 != 128):
                return False
        i = i + bytes_nbr
    return True
