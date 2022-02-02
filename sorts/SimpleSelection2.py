#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @Time     : 2/2/22 9:10 AM
# @Author   : solomon_mail@hotmail.com
# @File     : SimpleSelection2.py


def SimpleSelection(input_list):
    """
    O(n2)
    :param input_list:
    :return:
    """
    n = len(input_list)
    for i in range(1, n):
        tmp = input_list[i]
        for m in range(i - 1, -2, -1):
            if m == -1:
                input_list[0] = tmp
                break
            if input_list[m] > tmp:
                input_list[m + 1] = input_list[m]
            else:
                input_list[m + 1] = tmp
                break
    return input_list


if __name__ == "__main__":
    sorted_list = SimpleSelection([6,1,8,2,0,33,1,5,1,1,2,4])
    print(sorted_list)