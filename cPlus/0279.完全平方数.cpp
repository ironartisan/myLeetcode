

// 版本一
class Solution {
public:
    int numSquares(int n) {
        vector<int> dp(n + 1, INT_MAX);
        dp[0] = 0;
        for (int i = 0; i <= n; i++) { // 遍历背包
            for (int j = 1; j * j <= i; j++) { // 遍历物品
                dp[i] = min(dp[i - j * j] + 1, dp[i]);
            }
        }
        return dp[n];
    }
};

// 版本二

class Solution {
public:
    int numSquares(int n) {
        unordered_set<int> visited;  //记录访问过的节点值
        queue<int> q;
        int step = 0;
        q.push(n);
        while (q.size()) {
            int len = q.size();
            step++;
            while (len--) {
                int j = q.front();
                q.pop();
                for (int i = (int)sqrt(j); i > 0; i--) { // 从大到小遍历
                    int m = j - i * i;
                    if (m == 0) { // 如果找到数，直接返回
                        return step;
                    }
                    if (!visited.count(m)) { // 若没有记录过该值，加入队列，消除同一层中相同的数
                        visited.insert(m);
                        q.push(m);
                    }
                }
            }
        }
    return 0;
    }
};