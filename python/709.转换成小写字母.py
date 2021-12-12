#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/12/12 20:50 
class Solution:
    def toLowerCase(self, s: str) -> str:
        temp = []
        for ch in s:
            if 65 <= ord(ch) <= 90:
                ch = chr(ord(ch)| 32)
            temp.append(ch)
        return "".join(temp)