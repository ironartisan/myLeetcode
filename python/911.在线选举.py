#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/12/11 8:51
from collections import defaultdict
from typing import List


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        result = []
        vote_counts = defaultdict() # 候选人的得票数
        vote_counts[-1] = -1
        top = -1 # 领先的候选人
        for person in persons:
            vote_counts[person] = vote_counts.get(person, 0) + 1
            if vote_counts[person] >= vote_counts[top]:
                top = person
            result.append(top) # 不同时刻领先的候选人

        self.result = result
        self.times = times

    def q(self, t: int) -> int:
        left, right = 0, len(self.times) - 1
        while left < right:  # 找到满足 times[left] <= t 的最大的 l
            mid = left + (right - left + 1) // 2
            if self.times[mid] <= t:
                left = mid
            else:
                right = mid - 1
        return self.result[left]