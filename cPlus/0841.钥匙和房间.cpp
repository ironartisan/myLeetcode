class Solution
{
public:
    vector<bool> visited;
    int count;
    bool canVisitAllRooms(vector<vector<int>> &rooms)
    {
        int m = rooms.size();
        count = 0;
        visited.resize(m);
        dfs(rooms, 0);
        return count == m;
    }

    void dfs(vector<vector<int>> &rooms, int x)
    {
        visited[x] = true;
        count++;

        for (auto &val : rooms[x])
        {
            if (!visited[val])
            {
                dfs(rooms, val);
            }
        }
    }
};