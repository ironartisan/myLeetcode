#include <iostream>

using namespace std;

// Definition for singly-linked list.

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
 };
 
// 递归法

// class Solution {
// public:
//     ListNode* reverseList(ListNode* head) {
//         if (!head || !head -> next) {
//             return head;
//         }
//         ListNode* newHead = reverseList(head->next);
//         head->next->next = head;
//         head->next = nullptr;
//         return newHead;
//     }
// };

// 迭代法

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* pre = nullptr;
        ListNode* cur = head;
        while(cur) {
            ListNode* next = cur->next;
            cur->next = pre;
            pre = cur;
            cur = next;
        }
        return pre;
    }
};

int main() {
    std::cout << "Hello, World!" << std::endl;
    ListNode n1(0);
    ListNode n2(2);
    ListNode n3(5);
    ListNode n4(7);
    ListNode n5(10);
    n1.next = &n2;
    n2.next = &n3;
    n3.next = &n4;
    n4.next = &n5;
    
//    遍历一个链表
    ListNode* head = &n1;
    while(head){
        cout << head->val << ' ';
        head = head->next;
    }

    Solution solution;
    solution.reverseList(&n1);
    cout << endl;

    head = &n5;
    while(head){
        cout << head->val << ' ';
        head = head->next;
    }
    return 0;
}