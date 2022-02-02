#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @Time     : 2/2/22 8:43 AM
# @Author   : solomon_mail@hotmail.com
# @File     : FastSort2.py


def FastSort(input_list, lp, rp):
    """
    Worst: O(n2)
    Average: O(nlogn)
    :param input_list:
    :param lp:
    :param rp:
    :return:
    """
    if lp >= rp:
        return
    ori_lp = lp
    ori_rp = rp
    lp += 1
    while lp < rp:
        while lp < rp and input_list[rp] >= input_list[ori_lp]:
            rp -= 1
        while lp < rp and input_list[lp] <= input_list[ori_lp]:
            lp += 1
        if lp == rp:
            input_list[lp], input_list[ori_lp] = input_list[ori_lp], input_list[lp]
            FastSort(input_list, ori_lp, lp - 1)
            FastSort(input_list, lp + 1, ori_rp)
        else:
            input_list[lp], input_list[rp] = input_list[rp], input_list[lp]
    return input_list


if __name__ == "__main__":
    sorted_list = FastSort([6,1,8,2,0,33,1,5,1,1,2,4], 0, 11)
    print(sorted_list)