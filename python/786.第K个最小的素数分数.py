#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/11/29 19:53
import heapq
from functools import cmp_to_key
from typing import List


class Frac:
    def __init__(self, idx: int, idy: int, x: int, y: int) -> None:
        self.idx = idx
        self.idy = idy
        self.x = x
        self.y = y

    def __lt__(self, other: "Frac") -> bool:
        return self.x * other.y < self.y * other.x


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        q = [Frac(0, i, arr[0], arr[i]) for i in range(1, n)]
        heapq.heapify(q)

        for _ in range(k - 1):
            frac = heapq.heappop(q)
            i, j = frac.idx, frac.idy
            if i + 1 < j:
                heapq.heappush(q, Frac(i + 1, j, arr[i + 1], arr[j]))

        return [q[0].x, q[0].y]

class Solution1:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        def cmp(x, y):
            return -1 if x[0] * y[1] < x[1] * y[0] else 1
        n = len(arr)
        frac = list()
        for i in range(n):
            for j in range(i + 1, n):
                frac.append((arr[i], arr[j]))

        frac.sort(key=cmp_to_key(cmp))
        return list(frac[k - 1])

