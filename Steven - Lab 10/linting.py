"""
This code adds one to a number in a sequence
"""
def count(sequence, item):
    """
    Count the occurance of a given item in the sequence
    """
    result = 0
    for number in sequence:
        if number == item:
            result += 1
        return result
