#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
merge sort 归并排序
~~~~~~~~~~~~~~~~~~

归并排序是采用分治法的一个非常典型的应用。归并排序的思想就是先递归分解数组，再合并数组。

先考虑合并两个有序数组，基本思路是比较两个数组的最前面的数，谁小就先取谁，
取了后相应的指针就往后移一位。然后再比较，直至一个数组为空，
最后把另一个数组的剩余部分复制过来即可。

再考虑递归分解，基本思路是将数组分解成left和right，如果这两个数组内部数据是有序的，
那么就可以用上面合并数组的方法将这两个数组合并排序。如何让这两个数组内部是有序的？
可以再二分，直至分解出的小组只含有一个元素时为止，此时认为该小组内部已有序。
然后合并排序相邻二个小组即可。

"""

def merge_sort(arry):
    if len(arry) <= 1: return ary
    num = int(len(arry)/2)      #二分分解
    left = merge_sort(arry[:num])
    right = merge_sort(arry[num:])
    return merge(left, right)   #合并数组

def merge(left, right):
    '''合并操作，
    将两个有序数组left[]和right[]合并成一个大的有序数组'''
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result   
