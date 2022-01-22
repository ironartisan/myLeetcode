# 剑指 Offer 51. 数组中的逆序对

[题目链接](https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/)

在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

示例:
```
输入: [7,5,6,4]
输出: 5
```

## 思路

### 解法一：

暴力法求解，双层循环，若前面的数大于后面的数，则构成逆序关系，结果加1

```python
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        size = len(nums)
        if size < 2:
            return 0
        res = 0
        for i in range(size - 1):
            for j in range(i + 1, size):
                if nums[i] > nums[j]:
                    res += 1
        return res
```

### 解法二：
归并排序
1. 终止条件： 当 l≥r 时，代表子数组长度为 1 ，此时终止划分；
2. 递归划分： 计算数组中点 m ，递归划分左子数组 merge_sort(l, m) 和右子数组 merge_sort(m + 1, r) ；
3. 合并与逆序对统计：
    
   * 暂存数组 nums 闭区间 [i,r] 内的元素至辅助数组 tmp ；
   * 循环合并： 设置双指针 i , j分别指向左 / 右子数组的首元素；
        * 当 i=m+1时： 代表左子数组已合并完，因此添加右子数组当前元素 tmp[j] ，并执行 j=j+1；
        * 否则，当 j=r+1时： 代表右子数组已合并完，因此添加左子数组当前元素 tmp[i] ，并执行 i=i+1 ；
        * 否则，当 tmp[i]≤tmp[j]时： 添加左子数组当前元素 tmp[i] ，并执行 i=i+1；
        * 否则（即 tmp[i]>tmp[j]）时： 添加右子数组当前元素 tmp[j]，并执行 j=j+1 ；此时构成 m−i+1个「逆序对」，统计添加至 res；

[参考链接](https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/solution/jian-zhi-offer-51-shu-zu-zhong-de-ni-xu-pvn2h/)


```python
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(l, r):
            if l >= r:
                return 0
            m = (l + r) // 2
            res = merge_sort(l, m) + merge_sort(m + 1, r)
            i, j = l, m + 1
            tmp[l: r + 1] = nums[l:r + 1]
            for k in range(l, r + 1):
                if i == m - 1: # 左子树合并完
                    nums[k] = tmp[j] # 添加右子树元素
                    j += 1
                elif j == r + 1 or tmp[i] <= tmp[j]: # 右子树合并完或者左子树元素小于等于右子树元素
                    nums[k] = tmp[i] # 添加左子树元素
                    i += 1
                else:
                    nums[k] = tmp[j] # 添加右子树元素
                    j += 1
                    res += m - i + 1 # 统计逆序对
                return res

        tmp = [0] * len(nums)
        return merge_sort(0, len(nums) - 1)
```