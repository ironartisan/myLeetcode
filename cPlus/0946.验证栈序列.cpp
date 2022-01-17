#include <iostream>
#include <numeric>
#include <vector>

class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        int n = pushed.size();

        stack<int> stk;

        int count = 0;

        for (int num: pushed) {
            stk.push(num);
            while (!stk.empty() && count < n && stk.top() == popped[count]) {
                stk.pop();
                count++;
            }
        }
        return count == n;
    }
};