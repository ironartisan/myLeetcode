class Solution {

private:
    static constexpr int dirs[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    int m, n;
    int dfs(vector<vector<int>>& grid, int x, int y, bool &flag) {
        if (x < 0 || x>= m || y < 0 || y >= n || grid[x][y] != 1) { // 坐标不符合或单元格的值为0
            return 0;
        }
        if (x == 0 || x == m - 1 || y == 0 || y == n - 1) { // 若在边界上
            flag = true;
        }
        int res = 1;
        grid[x][y] = 0;
        for (int i = 0; i < 4; i++)
        {
            res += dfs(grid, x + dirs[i][0], y + dirs[i][1], flag);
        }
        return res;
    }
    
public:
    
    int numEnclaves(vector<vector<int>>& grid) {
        int ans = 0;
        m = grid.size();
        n = grid[0].size();
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) 
            {
                if (grid[i][j] == 1) {
                    bool flag = false; //用flag判断是否在边界上
                    int result = dfs(grid, i, j, flag);
                    if (!flag) {
                        ans += result;
                    }
                }
            }
        }
        return ans;
    }
};