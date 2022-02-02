#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @Time     : 2/2/22 8:37 AM
# @Author   : solomon_mail@hotmail.com
# @File     : BinarySearch2.py


def BinarySearch(input_list, target):
    """
    O(logn)
    :param input_list:
    :param target:
    :return:
    """
    n = len(input_list)
    lp, rp = 0, n - 1
    while lp <= rp:
        mid = (lp + rp) // 2
        if input_list[mid] < target:
            lp = mid + 1
        elif input_list[mid] > target:
            rp = mid - 1
        else:
            return mid
    return -1


if __name__ == "__main__":
    print("result: %d" % BinarySearch([1,4,7,9,13,16], 13))
