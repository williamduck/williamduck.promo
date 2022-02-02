#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @Time     : 2/2/22 8:54 AM
# @Author   : solomon_mail@hotmail.com
# @File     : InsertionSort2.py


def InsertionSort(input_list):
    """
    O(n2)
    :param input_list:
    :return:
    """
    n = len(input_list)
    for i in range(n):
        tmp = i
        for m in range(i + 1, n):
            if input_list[m] < input_list[tmp]:
                tmp = m
        input_list[tmp], input_list[i] = input_list[i], input_list[tmp]
    return input_list


if __name__ == "__main__":
    sorted_list = InsertionSort([6,1,8,2,0,33,1,5,1,1,2,4])
    print(sorted_list)