#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @Time     : 1/2/22 11:42 PM
# @Author   : solomon_mail@hotmail.com
# @File     : FastSort.py


class FastSortClass(object):
    """
    Time Complexity: O(n2)
    Average Time Complexity: O(nlogn)
    """
    @staticmethod
    def FastSort(input_list, left, right):
        if left >= right:
            return
        target = input_list[left]
        lp, rp = left, right
        lp += 1
        while lp < rp:
            """
            KEY: right point move first!!
            """
            while lp < rp and input_list[rp] >= target:
                rp -= 1
            while lp < rp and input_list[lp] <= target:
                lp += 1
            if lp == rp:
                input_list[left], input_list[lp] = input_list[lp], input_list[left]
            else:
                input_list[lp], input_list[rp] = input_list[rp], input_list[lp]
        FastSortClass.FastSort(input_list, left, lp - 1)
        FastSortClass.FastSort(input_list, lp + 1, right)
        return input_list

if __name__ == "__main__":
    sorted_list = FastSortClass.FastSort([6,1,8,2,0,33,1,5,1,1,2,4], 0, 11)
    print(sorted_list)
