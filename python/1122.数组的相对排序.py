#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/11/20 17:10
from typing import List
from collections import Counter


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr = []
        temp = []
        map = Counter(arr1)
        for digit in arr2:
            while map[digit] > 0:
                arr.append(digit)
                map[digit] -= 1
        for num in arr1:
            if num not in arr2:
                temp.append(num)
        temp.sort()
        return arr + temp


if __name__ == '__main__':
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    array = Solution().relativeSortArray(arr1, arr2)
    print(array)


