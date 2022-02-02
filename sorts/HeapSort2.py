#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @Time     : 2/2/22 8:52 AM
# @Author   : solomon_mail@hotmail.com
# @File     : HeapSort2.py
import heapq


def HeapSort(input_list):
    """
    O(nlogn)
    :param input_list:
    :return:
    """
    heapq.heapify(input_list)
    return [heapq.heappop(input_list) for i in range(len(input_list))]


if __name__ == "__main__":
    sorted_list = HeapSort([6,1,8,2,0,33,1,5,1,1,2,4])
    print(sorted_list)