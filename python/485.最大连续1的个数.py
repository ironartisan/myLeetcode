class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = -1
        ans = 0
        for j, num in enumerate(nums):
            if num == 1:
                ans = max(ans, j - i)
            else:
                i = j
        return ans

if __name__ == '__main__':
    nums = [1,1,0,1,1,1]
    res = Solution().findMaxConsecutiveOnes(nums)
    print(res)



