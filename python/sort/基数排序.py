#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/11/21 11:55
from typing import List


class Solution:
    def radixSort(self, nums: List[int]) -> List[int]:
        size = len(str(max(nums))) # 最大的数的位数，例如：2023位4位数

        for i in range(size):
            buckets = [[] for _ in range(10)]
            for num in nums:
                buckets[num // (10 ** i) % 10].append(num)
            nums.clear()
            for bucket in buckets:
                for num in bucket:
                    nums.append(num)
        return nums


if __name__ == '__main__':
    nums = [101, 0, 32, 53, 2023, 4]
    nums = Solution().radixSort(nums)
    print(nums)
