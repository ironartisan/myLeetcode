#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/11/19 16:55
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        size = len(nums)
        if size < 2:
            return 0
        res = 0
        for i in range(size - 1):
            for j in range(i + 1, size):
                if nums[i] > nums[j]:
                    res += 1
        return res

    def reversePairs1(self, nums: List[int]) -> int:
        def merge_sort(l, r):
            if l >= r:
                return 0
            m = (l + r) // 2
            res = merge_sort(l, m) + merge_sort(m + 1, r)
            i, j = l, m + 1
            tmp[l: r + 1] = nums[l:r + 1]
            for k in range(l, r + 1):
                if i == m - 1: # 左子树合并完
                    nums[k] = tmp[j] # 添加右子树元素
                    j += 1
                elif j == r + 1 or tmp[i] <= tmp[j]: # 右子树合并完或者左子树元素小于等于右子树元素
                    nums[k] = tmp[i] # 添加左子树元素
                    i += 1
                else:
                    nums[k] = tmp[j] # 添加右子树元素
                    j += 1
                    res += m - i + 1 # 统计逆序对
                return res

        tmp = [0] * len(nums)
        return merge_sort(0, len(nums) - 1)


if __name__ == '__main__':
    nums = [7, 5, 6, 4]
    ans = Solution().reversePairs1(nums)
    print(ans)