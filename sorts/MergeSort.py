#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @Time     : 1/2/22 11:06 PM
# @Author   : solomon_mail@hotmail.com
# @File     : MergeSort.py


class MergeSortClass(object):
    """
    Time Complexity: O(nlogn)
    """
    @staticmethod
    def MergeTwoPart(p1, p2):
        """
        Merge
        """
        len_p1 = len(p1)
        len_p2 = len(p2)
        lp1, lp2 = 0, 0
        merged_list = []
        while lp1 <= (len_p1 - 1) and lp2 <= (len_p2 - 1):
            if p1[lp1] <= p2[lp2]:
                merged_list.append(p1[lp1])
                lp1 += 1
            else:
                merged_list.append(p2[lp2])
                lp2 += 1
        while lp1 <= (len_p1 - 1):
            merged_list.append(p1[lp1])
            lp1 += 1
        while lp2 <= (len_p2 - 1):
            merged_list.append(p2[lp2])
            lp2 += 1
        return merged_list

    @staticmethod
    def MergeSort(input_list):
        """
        Divide
        """
        """
        Break Condition
        """
        if len(input_list) == 1:
            return input_list
        len_list = len(input_list)
        mid = len_list // 2
        """
        Divide
        """
        left_part = MergeSortClass.MergeSort(input_list[:mid])
        right_part = MergeSortClass.MergeSort(input_list[mid:])
        """
        Merge
        """
        return MergeSortClass.MergeTwoPart(left_part, right_part)


if __name__ == "__main__":
    sorted_list = MergeSortClass.MergeSort([6,1,8,2,0,33,1,5,1,1,2,4])
    print(sorted_list)
