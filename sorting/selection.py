#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
selection sort 选择排序
~~~~~~~~~~~~~~~~~~~~~~

1. 在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
2. 再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
3. 以此类推，直到所有元素均排序完毕。

"""

def select_sort(arry):
    n = len(arry)
    for i in range(0, n):
        min = i                  #最小元素下标标记
        for j in range(i+1, n):
            if arry[j] < arry[min]:
                min = j          #找到最小值的下标
        arry[min], arry[i] = arry[i], arry[min]
    return arry


# example
b = [x for x in range(1000)]     # array from 0 to 999
import random
random.shuffle(b)                # randomly shuffle
select_sort(b)

# timer
import time
tic = time.time()
select_sort(b)
toc = time.time() - tic
print(toc)
