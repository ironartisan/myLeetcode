#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/11/18 8:11

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """递归法"""
    def findTilt(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return 0,0
            l_sum, l_diff = dfs(root.left)
            r_sum, r_diff = dfs(root.right)
            return l_sum + r_sum + root.val, l_diff + r_diff + abs(r_sum - l_sum)
        return dfs(root)[1]


if __name__ == '__main__':
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    root.left = left
    root.right = right
    res = 0
    res = Solution().findTilt(root)
    print(res)
