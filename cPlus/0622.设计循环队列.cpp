class MyCircularQueue
{
public:
    int *queue;
    int front = 0, rear = 0; //让头指针指空
    int maxsize;
    MyCircularQueue(int k)
    {
        queue = new int[k + 1]; //用数组的形式来描述队列
        maxsize = k + 1;
    }

    bool enQueue(int value)
    {
        if (isFull())
            return false;
        rear = (rear + 1) % maxsize; 
        queue[rear] = value; //从尾部插入元素
        return true;
    }

    bool deQueue()
    {
        if (isEmpty())
            return false;
        front = (front + 1) % maxsize; // 删除元素
        return true;
    }

    int Front()
    {
        if (isEmpty())
            return -1;
        return queue[(front + 1) % maxsize];
    }

    int Rear()
    {
        if (isEmpty())
            return -1;
        return queue[rear];
    }

    bool isEmpty()
    {
        return front == rear; //这里当它们都为0的时候
    }

    bool isFull()
    {
        return ((rear + 1) % maxsize == front); // 元素满的情况
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */
