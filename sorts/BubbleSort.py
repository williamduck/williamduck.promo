#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @Time     : 1/2/22 5:23 PM
# @Author   : solomon_mail@hotmail.com
# @File     : BubbleSort.py


class BubbleSortClass(object):
    """
    Time Complexity: O(n2)
    """
    @staticmethod
    def BubbleSort(input_list):
        n = len(input_list)
        for i in range(n):
            for m in range(n - i - 1):
                if input_list[m] > input_list[m + 1]:
                    input_list[m], input_list[m + 1] = input_list[m + 1], input_list[m]
        return input_list


if __name__ == "__main__":
    sorted_list = BubbleSortClass.BubbleSort([6,1,8,2,0,33,1,5,1,1,2,4])
    print(sorted_list)
