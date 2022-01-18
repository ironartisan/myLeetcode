#include <iostream>
#include <vector>

// DFS
class Solution
{
public:
    int numIslands(vector<vector<char>>& grid)
    {
        int nr = grid.size();
        if (nr == 0)
        {
            return 0;
        }
        int nc = grid[0].size();

        int count = 0;

        for (int i = 0; i < nr; i++)
        {
            for (int j = 0; j < nc; j++)
            {
                if (grid[i][j] == '1') // 如果是1，则开始统计岛屿数量
                {
                    dfs(grid, i, j); // 执行DFS
                    count++;
                }
            }
        }
        return count;
    }

    void dfs(vector<vector<char>>& grid, int r, int c)
    {
        if (r < 0 || c < 0 || r >= grid.size() || c >= grid[0].size() || grid[r][c] == '0') {
            return;
        }
        grid[r][c] = '0'; // 将1变成0

        dfs(grid, r - 1, c);
        dfs(grid, r + 1, c);
        dfs(grid, r, c - 1);
        dfs(grid, r, c + 1);
    }
};

// BFS

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int count = 0;
        int m = grid.size();
        int n = grid[0].size();
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    bfs(grid, i, j);
                    count++;
                }
            }
        }

        return count;
    }

    void bfs(vector<vector<char>>& grid, int i, int j) {
        queue<pair<int, int>> q;
        q.push(make_pair(i, j));

        while (!q.empty()) {
            auto node = q.front();
            q.pop();
            int row = node.first;
            int col = node.second;

            if (row < 0 || col < 0 || row >= grid.size() || col >= grid[0].size() || grid[row][col] == '0') 
                continue;
            
            grid[row][col] = '0';
            q.push(make_pair(row + 1, col));
            q.push(make_pair(row, col + 1));
            q.push(make_pair(row, col - 1));
            q.push(make_pair(row - 1, col));

        }
    }
};