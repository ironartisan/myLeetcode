#include <iostream>

using namespace std;

class MyLinkedList
{
public:

    // 定义链表节点结构体
    struct LinkedNode
    {
        int val;
        LinkedNode *next;
        LinkedNode(int val):val(val), next(nullptr){}
    };
    
    // 初始化链表
    MyLinkedList()
    {
        _dumpyNode = new LinkedNode(0); //定义虚拟头节点
        _size = 0;
    }

    int get(int index)
    {
        if ((index > _size - 1) || index < 0) {
                return -1;
        }
        LinkedNode *cur = _dumpyNode->next;
        while(index--){
            cur = cur->next;
        }
        return cur->val;
    }

    void addAtHead(int val)
    {
        LinkedNode* newNode = new LinkedNode(val);
        newNode->next = _dumpyNode->next;
        _dumpyNode->next = newNode;
        _size++;
    }

    void addAtTail(int val)
    {
        LinkedNode* newNode = new LinkedNode(val);
        LinkedNode* cur = _dumpyNode;
        while(cur->next != nullptr){
            cur = cur->next;
        }
        cur->next = newNode;
        _size++;
    }

    void addAtIndex(int index, int val)
    {
        if (index > _size) { // index大于链表长度
            return;
        }
        LinkedNode* newNode = new LinkedNode(val);
        LinkedNode *cur = _dumpyNode;
        while(index--) {
            cur = cur->next;
        }
        newNode->next = cur->next;
        cur->next = newNode;
        _size++;
    }

    void deleteAtIndex(int index)
    {
        if(index > _size || index < 0) {
            return;
        }
        LinkedNode *cur = _dumpyNode;
        while(index--) {
            cur = cur->next;
        }
        LinkedNode *temp = cur->next;
        cur->next = cur->next->next;
        delete temp;
        _size--;
    }

private:
    int _size;
    LinkedNode *_dumpyNode;
};
