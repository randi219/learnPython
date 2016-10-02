#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
quick sort 快速排序
~~~~~~~~~~~~~~~~~~
1. 从数列中挑出一个元素作为基准数。
2. 分区过程，将比基准数大的放到右边，小于或等于它的数都放到左边。
3. 再对左右区间递归执行第二步，直至各区间只有一个数。
"""

def quick_sort(arry):
    return qsort(arry, 0, len(arry)-1)

def qsort(arry, left, right):
    #快排函数，ary为待排序数组，left为待排序的左边界，right为右边界
    if left >= right:
        return arry
    key = arry[left]         #取最左边的为基准数
    lp = left                #左指针
    rp = right               #右指针
    while lp < rp:
        while arry[rp] >= key and lp < rp:
            rp -= 1
        while arry[lp] <= key and lp < rp:
            lp += 1
        arry[lp], arry[rp] = arry[rp], arry[lp]
    arry[left], arry[lp] = arry[lp], arry[left]
    qsort(arry, left, lp-1)
    qsort(arry, rp+1, right)
    return arry
