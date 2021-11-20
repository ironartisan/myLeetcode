[题目链接](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/)
# 剑指 Offer 40. 最小的k个数
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

示例:
>输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]


## 思路

### 解法一：
快排法
```python
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        self.quick_sort(arr, 0, len(arr) - 1)
        return arr[:k]

    def quick_sort(self, nums,left, right):
        if left > right: return
        mid = self.partion(nums, left, right)
        self.quick_sort(nums, left, mid - 1)
        self.quick_sort(nums, mid + 1, right)

    def partion(self, nums, left, right):
        index = random.randint(left, right)
        pivot = nums[index]
        nums[index], nums[left] = nums[left], nums[index]
        i, j = left, right
        while i < j:
            while i < j and nums[j] >= pivot: j -= 1
            while i < j and nums[i] <= pivot: i += 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i], nums[left] = nums[left], nums[i]
        return i
```

