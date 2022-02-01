#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @Time     : 1/2/22 5:02 PM
# @Author   : solomon_mail@hotmail.com
# @File     : BinarySearch.py

class BinarySearchClass(object):
    """
    Time Complexity: O(logn)

    """

    @staticmethod
    def BinarySearch(input_list, target):
        input_list.sort()
        if len(input_list) == 0:
            return -1
        lp = 0
        rp = len(input_list) - 1
        """
        * Note: lp <= rp
        """
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
    print("result: %d" % BinarySearchClass.BinarySearch([1,4,7,9,13,16], 16))