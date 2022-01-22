class Solution {
public:
    int movingCount(int m, int n, int k) {
        vector<vector<bool>> visited(m, vector<bool>(n, false));
        queue<pair<int, int>> que; // 存放一对坐标{x, y}
        que.push({0, 0});
        visited[0][0] = true;
        int res = 0;
        while(!que.empty()){
            pair<int, int> front = que.front(); que.pop();
            int x = front.first;
            int y = front.second;
            res++;
            // 遍历该位置(x, y)相邻的四个位置
            for(auto d:directions){
                int newX = x + d[0];
                int newY = y + d[1];
                if(newX < 0 || newX > m-1 || newY < 0 || newY > n-1 || 
                    bitSum(newX) + bitSum(newY) > k || visited[newX][newY]){
                        continue;
                }
                que.push({newX, newY});
                visited[newX][newY] = true;
            }
        }
        return res;
    }
private:
    vector<vector<int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}}; // 上下左右
    int bitSum(int x){ // 数位和
        int sum = 0;
        while(x != 0){
            sum += x % 10;
            x /= 10;
        }
        return sum;
    }
};