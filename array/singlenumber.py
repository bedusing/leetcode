# coding:utf-8

def get_single_number(number_list):
    """
    Given an array of integers, every element appears twice except for one. Find that single one.
    Note:
    Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
    """
    return reduce(lambda x, y: x ^ y, number_list)

def get_single_number1(number_list):
    """
    Given an array of integers, every element appears three times except for one. Find that single one.
    Note:
    Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
    """
    
    pass

print get_single_number([1, 2, 4, 2, 4])
