#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @Time     : 2/2/22 8:58 AM
# @Author   : solomon_mail@hotmail.com
# @File     : MergeSort2.py


def Merge(left_part, right_part):
    rst = []
    lp, rp, ln, rn = 0, 0, len(left_part) - 1, len(right_part) - 1
    while lp <= ln and rp <= rn:
        if left_part[lp] < right_part[rp]:
            rst.append(left_part[lp])
            lp += 1
        else:
            rst.append(right_part[rp])
            rp += 1
    while lp <= ln:
        rst.append(left_part[lp])
        lp += 1
    while rp <= rn:
        rst.append(right_part[rp])
        rp += 1
    return rst


def MergeSort(input_list):
    """
    O(nlogn)
    :param input_list:
    :return:
    """
    n = len(input_list)
    if n <= 1:
        return input_list
    mid = n // 2
    left_part = input_list[:mid]
    right_part = input_list[mid:]
    return Merge(MergeSort(left_part), MergeSort(right_part))


if __name__ == "__main__":
    sorted_list = MergeSort([6,1,8,2,0,33,1,5,1,1,2,4])
    print(sorted_list)
