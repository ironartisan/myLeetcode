#include <iostream>
#include <vector>
using namespace std;

// 解法1

// class Solution
// {
// public:

//     void maxHeapify(vector<int> &nums, int index, int heapSize)
//     {
//         int left = 2 * index + 1, right = 2 * index + 2, largest = index;
//         if (left < heapSize && nums[left] > nums[largest])
//         {
//             largest = left;
//         }
//         if (right < heapSize && nums[right] > nums[largest])
//         {
//             largest = right;
//         }
//         if (largest != index)
//         {
//             swap(nums[index], nums[largest]);
//             maxHeapify(nums, largest, heapSize); // 递归调整
//         }
//     }

//     void buildMaxHeap(vector<int> &nums, int heapSize)
//     {
//         for (int i = heapSize / 2; i >= 0; i--)
//         {
//             maxHeapify(nums, i, heapSize); // 创建大根堆
//         }
//     }

//     int findKthLargest(vector<int> &nums, int k)
//     {
//         int heapSize = nums.size();
//         buildMaxHeap(nums, heapSize);
//         for (int i = nums.size() - 1; i >= nums.size() - k + 1; --i) // 调整 k - 1 次
//         {
//             swap(nums[0], nums[i]);
//             --heapSize;
//             maxHeapify(nums, 0, heapSize);
//         }
//     }
//     return nums[0];
// };

// 解法2
class Solution
{
public:
    int findKthLargest(vector<int> &nums, int k)
    {
        int heapSize = nums.size();
        // 建成大根堆
        for (int i = heapSize / 2; i >= 0; i--)
        {
            sink(nums, i, heapSize);
        }
        for (int i = nums.size() - 1; i >= nums.size() - k + 1; i--)
        {
            swap(nums[0], nums[i]);
            heapSize--;
            sink(nums, 0, heapSize);
        }

        return nums[0];
    }

private:
    // 上浮 从下到上调整堆
    void swim(vector<int> &heap, int i)
    {
        while (i > 0 && heap[i] < heap[(i - 1) / 2])
        { // 与父节点进行比较
            swap(heap[i], heap[(i - 1) / 2]);
            i = (i - 1) / 2;
        }
    }

    // 下沉 从下到上调整堆
    void sink(vector<int> &heap, int i, int N)
    {
        while (2 * i + 1 < N)
        {
            int j = 2 * i + 1;
            if (j + 1 < N && heap[j + 1] > heap[j])
            { // 从两个节点中找到最大的元素
                j++;
            }
            if (heap[i] > heap[j])
            {
                break;
            }
            swap(heap[i], heap[j]);
            i = j;
        }
    }
};

int main()
{
    vector<int> nums = {2, 1};
    int k = 2;
    Solution solution;
    int x = solution.findKthLargest(nums, k);
    cout << x;
    return 0;
}