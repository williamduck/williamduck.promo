#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @Time     : 1/2/22 7:57 PM
# @Author   : solomon_mail@hotmail.com
# @File     : InsertionSort.py


class InsertionSortClass(object):
    """
    O(n2)
    """
    @staticmethod
    def InsertionSort(input_list):
        n = len(input_list)
        for i in range(n):
            tmp = input_list[i]
            for j in range(i - 1, -2, -1):
                if j != -1 and input_list[j] > tmp:
                    input_list[j + 1] = input_list[j]
                else:
                    input_list[j + 1] = tmp
                    break
        return input_list


if __name__ == "__main__":
    sorted_list = InsertionSortClass.InsertionSort([6,1,8,2,0,33,1,5,1,1,2,4])
    print(sorted_list)