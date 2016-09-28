#!/usr/bin/env python


# bubble sort 冒泡算法
# 1. 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
# 2. 对第0个到第n-1个数据做同样的工作。这时，最大的数就“浮”到了数组最后的位置上。
# 3. 针对所有的元素重复以上的步骤，除了最后一个。
# 4. 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

def bubble_sort(arry):
    n = len(arry)
    for i in range(n):
        for j in range(1, n-i):
            if arry[j-1] > arry[j]:
                arry[j-1], arry[j] = arry[j], arry[j-1]
    return arry

# example
b = [x for x in range(1000)]     # array from 0 to 999
import random
random.shuffle(b)                # randomly shuffle
bubble_sort(b)

# timer
import time
tic = time.time()
bubble_sort(b)
toc = time.time() - tic
print(toc)


#优化1：某一趟遍历如果没有数据交换，则说明已经排好序了，
#      因此不用再进行迭代了。用一个标记记录这个状态即可。
def bubble_sort2(arry):
    n = len(arry)
    for i in range(n):
        flag = 1
        for j in range(1, n-i):
            if arry[j-1] > arry[j]:
                arry[j-1], arry[j] = arry[j], arry[j-1]
                flag = 0
        if flag :
            break
    return arry

# the same example
tic = time.time()
bubble_sort2(b)
toc = time.time() - tic
print(toc)


#优化2：记录某次遍历时最后发生数据交换的位置，这个位置之后
#      的数据显然已经有序，不用再排序了。因此通过记录最后
#      发生数据交换的位置就可以确定下次循环的范围了。
def bubble_sort3(arry):
    n = len(arry)
    k = n                           # k为循环的范围，初始值n
    for i in range(n):
        flag = 1
        for j in range(1, k):       # 只遍历到最后交换的位置即可
            if arry[j-1] > arry[j]:
                arry[j-1], arry[j] = arry[j], arry[j-1]
                k = j               # 记录最后交换的位置
                flag = 0
        if flag :
            break
    return arry

# the same example
tic = time.time()
bubble_sort3(b)
toc = time.time() - tic
print(toc)
