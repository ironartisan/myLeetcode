# 剑指 Offer 45. 把数组排成最小的数

[题目链接](https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/)


输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

示例 1:
```
输入: [10,2]
输出: "102"
```

## 思路

本题可以理解为一个字典序的排序问题,可以修改快排的比较方法。
比较方法：设置pivot节点，一趟快拍后，pivot之前的所有元素+pivot组合产生的数字都应小于pivot+之前的元素。 pivot之后的元素同理。

### 解法一：

```python
class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def quick_sort(l, r):
            if l >= r: return
            i, j = l, r
            while i < j:
                while strs[j] + strs[l] >= strs[l] + strs[j] and i < j: j -= 1
                while strs[i] + strs[l] >= strs[l] + strs[i] and i < j: i += 1
                strs[i], strs[l] = strs[l], strs[i]
            strs[i], strs[l] = strs[l], strs[i]
            quick_sort(l, i - 1)
            quick_sort(i + 1, r)

        strs = [str(num) for num in nums]
        quick_sort(0, len(strs) - 1)
        return ''.join(strs)
```

