#include <iostream>

class Solution
{
public:
    vector<int> dailyTemperatures(vector<int> &temperatures)
    {
        int n = temperatures.size();
        stack<int> stk;
        vector<int> res(n);
        for (int i = 0; i < n; i++)
        {
            while (!stk.empty() && temperatures[i] > temperatures[stk.top()]) // 找到更大的元素
            {
                int index = stk.top(); 
                res[index] = i - index; //下标差值
                stk.pop();
            }
            stk.push(i);
        }
        return res;
    }
}；