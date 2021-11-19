#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/11/19 15:54
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        if not score: return []
        # 对数组进行排序
        score_sort = list(sorted(score, reverse=True))
        # 名次
        rank_list = ["Gold Medal", "Silver Medal", "Bronze Medal"]+[str(i+4) for i in range(len(score)-3)]
        # 将两个数组拼接成字典
        map = dict(zip(score_sort, rank_list))
        result = [map[num] for num in score]
        return result


if __name__ == '__main__':
    score = [5, 4, 3, 2, 1]
    ranks = Solution().findRelativeRanks(score)
    for rank in ranks:
        print(rank)
