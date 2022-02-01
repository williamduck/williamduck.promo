#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @Time     : 1/2/22 10:55 PM
# @Author   : solomon_mail@hotmail.com
# @File     : HeapSort.py
import heapq


class HeapSortClass(object):
    """
    TimeComplexity: O(nlogn)
    """
    @staticmethod
    def HeapSort(input_list):
        heapq.heapify(input_list)
        return [heapq.heappop(input_list) for i in range(len(input_list))]


if __name__ == "__main__":
    sorted_list = HeapSortClass.HeapSort([6,1,8,2,0,33,1,5,1,1,2,4])
    print(sorted_list)
