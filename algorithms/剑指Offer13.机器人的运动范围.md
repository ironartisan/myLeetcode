# 剑指Offer13.机器人的运动范围

[题目链接](https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/)

地上有一个 m 行 n 列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？


示例:

```
输入：m = 2, n = 3, k = 1
输出：3
```


## 思路

### 解法一：

本题为坐标移动问题，可使用 `BFS`、`DFS` 或 `DP` 法。

这里给出BFS解法。

1. 使用队列存储坐标，并使用数组存储访问标记；
2. 先将初始坐标 `push` 到队列中，依次遍历相邻的四个位置，判断是否能满足条件；
3. 若满足条件，则加入到队列中，并设置访问标记。

{% raw %}
```c++
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
```
{% endraw %}
## 其他题解
* <https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/solution/mian-shi-ti-13-ji-qi-ren-de-yun-dong-fan-wei-dfs-b/>