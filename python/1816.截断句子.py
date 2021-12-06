#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/12/6 9:28


class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        return " ".join(s.split(" ")[:k])


if __name__ == '__main__':
    s = "Hello how are you Contestant"
    k = 4
    print(Solution().truncateSentence(s, k))