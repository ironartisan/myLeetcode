#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    void reverseString(vector<char> &s)
    {
        int left = 0;
        int right = s.size() - 1;
        while (left < right)
        {
            swap(s[left], s[right]);
            left++;
            right--;
        }
    }
};

int main()
{
    vector<char> s = {'h', 'e', 'l', 'l', 'o'};
    Solution solution;
    solution.reverseString(s);
    for (int i = 0; i < s.size(); i++)
    {
        cout << s[i] << endl;
    }
}