#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/12/13 18:54 
class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rowMax = list(map(max, grid))
        colMax = list(map(max, zip(*grid)))
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
               ans += min(rowMax[i], colMax[j]) - grid[i][j]
        return ans