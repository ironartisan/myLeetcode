class Solution {
public:
    static constexpr int dirs[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int res = 0;

        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                res = max(res, dfs(grid, i, j)); // 取最大的结果
            }
        }
        return res;
    }

    int dfs(vector<vector<int>>& grid, int i, int j) {
        if (i < 0 || j < 0 || i >= grid.size() || j >= grid[0].size() || grid[i][j] != 1) { // 不满足条件
            return 0;
        }
        grid[i][j] = 0; // 将遍历过的单元格置为0
        int ans = 1;
        for (int index = 0; index < 4; index++) {
            int ni = i + dirs[index][0];
            int nj = j + dirs[index][1];
            ans += dfs(grid, ni, nj); //递归遍历并计算单元格的个数
        }
        return ans;
    }
    
};