class Solution
{
public:
    int count = 0;

    int findTargetSumWays(vector<int> &nums, int target)
    {
        dfs(nums, target, 0, 0);
        return count;
    }

    void dfs(vector<int> &nums, int target, int index, int sum)
    {
        if (index == nums.size())
        {
            if (sum == target)
            {
                count++;
            }
        }
        else
        {
            dfs(nums, target, index + 1, sum + nums[index]);
            dfs(nums, target, index + 1, sum - nums[index]);
        }
    }
};