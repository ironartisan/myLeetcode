#include <iostream>

using namespace std;

// Definition for singly-linked list.

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (head == nullptr || head->next == nullptr) {
            return false;
        }
        ListNode* slow = head;
        ListNode* fast = head->next; // 与下方 while 循环对应，若为 head,则循环不执行
        while (slow != fast) { // 判断链表成环
            if (fast == nullptr || fast->next == nullptr) { // 链表不成环，直接return
                return false;
            }
            slow = slow->next;
            fast = fast->next->next;
        }
        return true;
    }
};