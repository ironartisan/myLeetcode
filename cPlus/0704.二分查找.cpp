#include <iostream>
#include <vector>

// 有序的（升序）整型数组,如果目标值存在返回下标，否则返回 -1。
class Solution
{
public:
    int search(vector<int> &nums, int target)
    {

        int left = 0;
        int right = nums.size() - 1; // 定义target在左闭右闭的区间里，[left, right]
        while (left <= right)
        {
            int mid = left + ((right - left) / 2); // 防止溢出 等同于(left + right)/2
            if (nums[mid] == target)
            {
                return mid;
            }
            else if (nums[mid] > target)
            {
                right = mid - 1;
            }
            else
            {
                left = mid + 1;
            }
        }
    }
    return -1;
};
