#include <iostream>
#include <vector>
#include <unordered_map>
#include <stack>

using namespace std;

// 暴力法求解

// class Solution
// {
// public:
//     vector<int> nextGreaterElement(vector<int> &nums1, vector<int> &nums2)
//     {
//         int m = nums1.size();
//         int n = nums2.size();

//         vector<int> res(m);
//         for (int i = 0; i < m; i++)
//         {
//             int j = 0;
//             while (j < n && nums2[j] != nums1[i])
//             { // 找到num2中相等的数
//                 ++j;
//             }
//             int k = j + 1;
//             while (k < n && nums2[k] < nums2[j])
//             { // 向后寻找
//                 ++k;
//             }
//             res[i] = k < n ? nums2[k] : -1; // k<n 代表找到，否则k=n没找到
//         }
//         return res;
//     }
// };

class Solution
{
public:
    vector<int> nextGreaterElement(vector<int> &nums1, vector<int> &nums2)
    {
        unordered_map<int, int> hashmap;
        stack<int> stk;
        int m = nums1.size();
        int n = nums2.size();

        for (int i = n - 1; i >= 0; --i)
        {
            int num = nums2[i];
            while (!stk.empty() && num >= stk.top()) {
                stk.pop();
            }
            hashmap[num] = stk.empty() ? -1 : stk.top();
            stk.push(num);
        }
        vector<int> res(m);

        for (int i = 0; i < m; ++i) {
            res[i] = hashmap[nums1[i]];
        }
        
        return res;
    }
};

int main()
{
    Solution solution;
    vector<int> nums1 = {2, 4};
    vector<int> nums2 = {1, 2, 3, 4};
    vector<int> res = solution.nextGreaterElement(nums1, nums2);
    for (int num : res)
    {
        std::cout << num << std::endl;
    }
    return 0;
}