#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @Time     : 2/2/22 8:41 AM
# @Author   : solomon_mail@hotmail.com
# @File     : BubbleSort2.py


def BubbleSort(input_list):
    """
    O(n2)
    :param input_list:
    :return:
    """
    n = len(input_list)
    for i in range(n):
        for m in range(n - i - 1):
            if input_list[m + 1] < input_list[m]:
                input_list[m + 1], input_list[m] = input_list[m], input_list[m + 1]
    return input_list


if __name__ == "__main__":
    sorted_list = BubbleSort([6,1,8,2,0,33,1,5,1,1,2,4])
    print(sorted_list)
