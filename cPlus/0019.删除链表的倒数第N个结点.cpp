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
    ListNode *removeNthFromEnd(ListNode *head, int n)
    {
        ListNode *dumpyNode = new ListNode(-1, head);
        ListNode *fast = head, *slow = dumpyNode;

        while (n-- > 0)
        {
            fast = fast->next;
        }

        while (fast != nullptr) 
        {
            fast = fast->next;
            slow = slow->next;
        }
        slow->next = slow->next->next;
        return dumpyNode->next;
    }
};