#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @Time     : 1/2/22 5:54 PM
# @Author   : solomon_mail@hotmail.com
# @File     : SimpleSelection.py


class SimpleSelectionSortClass(object):
    """
    Time Complexity: O(n2)
    """
    @staticmethod
    def SimpleSelectionSort(input_list):
        n = len(input_list)
        for i in range(n):
            min_val = i
            for m in range(i + 1, n):
                if input_list[m] < input_list[min_val]:
                    min_val = m
            input_list[i], input_list[min_val] = input_list[min_val], input_list[i]
        return input_list


if __name__ == "__main__":
    sorted_list = SimpleSelectionSortClass.SimpleSelectionSort([6,1,8,2,0,33,1,5,1,1,2,4])
    print(sorted_list)
