#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/12/5 9:10
from typing import List

MOD = 1337


class Solution:

    def superPow(self, a: int, b: List[int]) -> int:
        return self.dfs(a, b, len(b) - 1)

    def dfs(self, a: int, b: List[int], u: int) -> int:
        if u == -1: return 1
        return self.pow(self.dfs(a, b, u -1), 10) * self.pow(a, b[u]) % MOD

    def pow(self, a: int, x: int) -> int:
        ans = 1
        a %= MOD
        while x > 0:
            ans = ans * a % MOD
            x -= 1
        return ans

    def pow2(self, a: int, x: int) -> int:
        ans = 1
        a %= MOD
        while x != 0:
            if (x & 1) != 0:
                ans = ans * a % MOD
            a = a * a % MOD
            x >>= 1
        return ans


if __name__ == '__main__':
    a = 2147483647
    b = [2, 0, 0]
    print(Solution().superPow(a, b))
