#include<iostream>
#include<vector>

using namespace std;

class Solution {

public:
    string removeDuplicateLetters(string s) {
        vector<int> visit(26), num(26);
        for (char ch: s) {
            num[ch - 'a']++;
        }
        string stk;

        for (char ch : s) {

            if (!visit(ch - 'a')) { // 
                while (!stk.empty() && stk.back() > ch) { // 字典序大于ch，出栈

                    stk.pop_back();
                }
            
            
                visit[ch - 'a'] = 1;
                stk.push_back(ch);
            }
            num[ch - 'a'] -= 1;
        }
        return stk;
    }
}