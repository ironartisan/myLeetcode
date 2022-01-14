
// 辅助栈

// class MinStack {
//     stack<int> valStack;
//     stack<int> minStack;
// public:
//     MinStack() {
//         minStack.push(INT_MAX); // 初始化的时候填入最大值，便于后续比较
//     }

//     void push(int val) {
//         valStack.push(val);
//         minStack.push(min(minStack.top(), val));
//     }

//     void pop() {
//         valStack.pop();
//         minStack.pop();
//     }

//     int top() {
//         return valStack.top();
//     }

//     int getMin() {
//         return minStack.top();
//     }
// };

// 辅助数组

class MinStack
{
    vector<int> vec;
    vector<int> minVec;

public:
    MinStack()
    {
    }

    void push(int val)
    {
        vec.push_back(val);
        if (minVec.size() == 0)
        {
            minVec.push_back(val);
        }
        else if (val <= minVec[minVec.size() - 1])
        { // // 小于等于，防止多个最小值的情况
            minVec.push_back(val);
        }
    }

    void pop()
    {
        if (vec.size() == 0)
        { // 防止越界
            return;
        }
        if (vec[vec.size() - 1] == minVec[minVec.size() - 1]) //
        {
            minVec.pop_back();
        }
        vec.pop_back();
    }

    int top()
    {
        return vec[vec.size() - 1];
    }

    int getMin()
    {
        return minVec[minVec.size() - 1];
    }
};
