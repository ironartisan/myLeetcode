class Solution
{
public:
    int m, n;
    int closedIsland(vector<vector<int>> &grid)
    {
        int res = 0;
        m = grid.size();
        n = grid[0].size();

        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (grid[i][j] == 0)
                {
                    res += dfs(grid, i, j);
                }
            }
        }
        return res;
    }

    int dfs(vector<vector<int>> &grid, int x, int y)
    {
        if (x < 0 || x >= m || y < 0 || y >= n)
        {
            return 0;
        }
        if (grid[x][y] == 1)
        { //碰到水域(值为1的点)就返回封闭岛屿个数1，表示该岛屿可能就是一个封闭岛屿
            return 1;
        }
        grid[x][y] = 1;

        // 如果碰到陆地(值为0的点)就继续向该陆地的四个方向遍历，同时将该陆地标记为1，表示这个位置已经遍历过了。
        int vx[] = {0, 1, 0, -1};
        int vy[] = {1, 0, -1, 0};
        int res = 1;
        for (int i = 0; i < 4; i++)
        {
            res = min(res, dfs(grid, x + vx[i], y + vy[i])); // 四个方向进行遍历，若到达边界，则证明不是封闭岛屿，返回0
        }
        return res;
    }

    int bfs(vector<vector<int>> &grid, int x, int y)
    {
        int res = 1;
        queue<vector<int>> q;
        q.push({x, y});

        while (!q.empty())
        {
            vector<int> pos(q.front());
            q.pop();
            grid[pos[0]][pos[1]] = 1;
            int vx[] = {0, 1, 0, -1};
            int vy[] = {1, 0, -1, 0};

            for (int i = 0; i < 4; i++)
            {
                int nx = pos[0] + vx[i];
                int ny = pos[1] + vy[i];

                if (nx < 0 || nx >= m || ny < 0 || ny >= n)
                { // 若达到边界上，则证明不是封闭岛屿
                    res = 0;
                    continue;
                }

                if (grid[nx][ny] == 0)
                { // 将其他邻近的陆地添加到队列中
                    q.push({nx, ny});
                }
            }
        }
        return res;
    }
};