#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/12/7 15:04
from typing import List


class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        border = []
        origin_color = grid[row][col]
        visited[row][col] = True
        self.dfs(grid, row, col, visited, border, origin_color)
        for x, y in border:
            grid[x][y] = color
        return grid

    def dfs(self, grid, x, y, visited, borders, origin_color):
        is_border = False
        m, n = len(grid), len(grid[0])
        direction = ((-1, 0), (1, 0), (0, -1), (0, 1))
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < m and 0 <= ny < n and grid[nx][ny] == origin_color):
                is_border = True
            elif not visited[nx][ny]:
                visited[nx][ny] = True
                self.dfs(grid, nx, ny, visited, borders, origin_color)
        if is_border:
            borders.append((x, y))

