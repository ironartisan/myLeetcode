
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        if (amount == 0) return 0;
        unordered_set<int> visited;  //记录访问过的节点值
        queue<int> q;
        int step = 0;
        q.push(amount);
        while (q.size()) {
            int len = q.size();
            step++;
            while (len--) {
                int j = q.front();
                q.pop();
                for (int coin : coins) { // 遍历硬币
                    int m = j - coin;
                    if (m == 0) { // 如果凑齐，直接返回
                        return step;
                    }
                    if (m < 0 ) {
                        continue;
                    }
                    if (!visited.count(m)) { // 若没有记录过该值，加入队列，消除同一层中相同的数
                        visited.insert(m);
                        q.push(m);
                    }
                }
            }
        }
    return -1;
        
    }
};