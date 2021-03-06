class Solution
{
public:
    vector<vector<int>> P, A, ans;
    int n, m;
    vector<vector<int>> pacificAtlantic(vector<vector<int>> &heights)
    {
        m = heights.size();
        n = heights[0].size();

        P = A = vector<vector<int>>(m, vector<int>(n, 0));

        for (int i = 0; i < m; ++i)
        {
            dfs(heights, P, i, 0);
            dfs(heights, A, i, n - 1);
        }
        for (int j = 0; j < n; ++j)
        {
            dfs(heights, P, 0, j);
            dfs(heights, A, m - 1, j);
        }
        return ans;
    }

    void dfs(vector<vector<int>> &heights, vector<vector<int>> &visited, int i, int j)
    {
        if (visited[i][j]) { // 之前访问过，忽略
            return;
        } 
            
        visited[i][j] = 1;
        if (P[i][j] && A[i][j]) // 均可达
        {
            ans.push_back({i, j});
        }
        //上下左右深搜
        if (i - 1 >= 0 && heights[i - 1][j] >= heights[i][j]) {
            dfs(heights, visited, i - 1, j);
        }

        if (i + 1 < m && heights[i + 1][j] >= heights[i][j]) {
            dfs(heights, visited, i + 1, j);
        }

        if (j - 1 >= 0 && heights[i][j - 1] >= heights[i][j]) {
            dfs(heights, visited, i, j - 1);
        }
            
        if (j + 1 < n && heights[i][j + 1] >= heights[i][j]) {
            dfs(heights, visited, i, j + 1);
        }
            
    }
};