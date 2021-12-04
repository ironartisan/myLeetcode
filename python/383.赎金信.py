#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/12/4 20:28 
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        return not Counter(ransomNote) - Counter(magazine)


if __name__ == '__main__':
    ransomNote = "aa"
    magazine = "aab"
    print(not Counter(ransomNote) - Counter(magazine))