class MyStack {
public:
    queue<int> queue1;
    queue<int> queue2;

    /** Initialize your data structure here. */
    MyStack() {

    }

    /** Push element x onto stack. */
    void push(int x) {
        queue2.push(x);
        while (!queue1.empty()) {
            queue2.push(queue1.front()); // 将queue1中的元素 push 到 queue2，相当于 x 在 front端，对应栈顶
            queue1.pop();
        }
        swap(queue1, queue2);
    }
    
    /** Removes the element on top of the stack and returns that element. */
    int pop() {
        int val = queue1.front();
        queue1.pop();
        return val;
    }
    
    /** Get the top element. */
    int top() {
        int val = queue1.front();
        return val;
    }
    
    /** Returns whether the stack is empty. */
    bool empty() {
        return queue1.empty();
    }
};

