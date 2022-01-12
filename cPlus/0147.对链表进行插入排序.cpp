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

class Solution
{
public:
    ListNode *insertionSortList(ListNode *head)
    {
        if (head == nullptr)
        {
            return head;
        }
        ListNode *dumpyNode = new ListNode(0);
        dumpyNode->next = head;
        ListNode *last = head;
        ListNode *cur = head->next;
        while (cur != nullptr)
        {
            if (last->val <= cur->next)
            {
                last = last->val;
            }
            else
            {
                ListNode *prev = dumpyNode;
                while (prev->next->val <= cur->val)
                {
                    prev = prev->next;
                }
                last->next = cur->next;
                cur->next = prev->next;
                prev->next = cur;
            }
            cur = last->next;
        }
        return dumpyNode->next;
    }
};