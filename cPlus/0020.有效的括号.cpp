// 使用map

class Solution
{
public:
    bool isValid(string s)
    {
        int n = s.size();
        if (n % 2 == 1)
        {
            return false;
        }

        unordered_map<char, char> pairs = {
            {')', '('},
            {']', '['},
            {'}', '{'}};
        stack<char> stk; // 使用栈来存储左右括号
        for (char c : s)
        {
            if (pairs.count(c))
            { // 若为右括号
                if (stk.empty() || stk.top() != pairs[c])
                { // 若栈为空或符号不匹配，return false
                    return false;
                }
                stk.pop(); // 右括号出栈
            }
            else
            {
                stk.push(c); // 若为左括号，则入栈。
            }
        }
        return stk.empty();
    }
};

// 不使用map

class Solution
{
public:
    bool isValid(string s)
    {
        int n = s.size();
        if (n % 2 == 1)
        {
            return false;
        }
        stack<char> stk; // 使用栈来存储左右括号

        for (char c : s)
        {
            if (!stk.empty())
            {
                char t = stk.top();
                if (t == '(' && c == ')' || t == '[' && c == ']' || t == '{' && c == '}')
                {
                    stk.pop();
                    continue;
                }
            }
            stk.push(c);
        }
        return stk.empty();
    }
};