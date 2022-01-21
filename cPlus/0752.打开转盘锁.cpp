#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    string s, t;
    unordered_set<string> st;

    int openLock(vector<string> &deadends, string target)
    {
        s = "0000";
        t = target;

        if (s == t)
        {
            return 0; // 初始时满足条件
        }
        for (const auto &d : deadends)
        {
            st.insert(d);
        }

        if (st.count(s))
        {
            return -1;
        }
        int ans = bfs();

        return ans;
    }

    // bfs逻辑
    int bfs()
    {
        queue<string> q1, q2;              // 双向队列
        unordered_map<string, int> m1, m2; // 统计次数

        q1.push(s);
        m1[s] = 0;
        q2.push(t);
        m2[t] = 0;

        // while (q1.size() != 0 && q2.size() != 0)
        while (q1.size() and  q2.size())
        { // 若 q1 和 q2 都为空还搜索不到，则证明无法走通
            int t = -1;
            if (q1.size() <= q2.size())
            {
                t = update(q1, m1, m2);
            }
            else
            {
                t = update(q2, m2, m1);
            }
            if (t != -1)
            {
                return t;
            }
            
        }
        return -1;
        
    }

    int update(queue<string> &q, unordered_map<string, int> &cur, unordered_map<string, int> &other)
    {
        int m = q.size();
        while (m-- > 0)
        {
            string t = q.front(); // 队列中去除一个四位数
            q.pop();
            int step = cur[t];
            for (int i = 0; i < 4; i++)
            { // 四位数
                for (int j = -1; j <= 1; j++)
                { // 三种可能，+1， 0， -1
                    if (j == 0)
                    {
                        continue;
                    }
                    int origin = t[i] - '0';
                    int next = (origin + j) % 10;
                    if (next == -1)
                    { // 若为0，j= -1,则应为9
                        next = 9;
                    }
                    string copy = t;
                    copy[i] = '0' + next; // 转化为字符
                    if (st.count(copy) or cur.count(copy))
                    { // 不可取或之前走过
                        continue;
                    }
                    if (other.count(copy))
                    { //两个队列搜索到同样的数，证明可以走通
                        return step + 1 + other[copy];
                    }
                    else
                    {
                        q.push(copy);
                        cur[copy] = step + 1;
                    }
                }
            }
        }
        return -1;
    }
};

