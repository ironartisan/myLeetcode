#include <unordered_map>

// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = nullptr;
        random = nullptr;
    }
};


// class Solution {
// public:
    
//     unordered_map<Node*, Node*> cacheNode;

//     Node* copyRandomList(Node* head) {
//         if (head == nullptr) {
//             return nullptr;
//         }
//         if (!cacheNode.count(head)) {
//             Node *node = new Node(head->val);
//             cacheNode[head] = node;
//             node->next = copyRandomList(head->next);
//             node->random = copyRandomList(head->random);
//         }
//         return cacheNode[head];
//     }
// };

class Solution {
public:
    
    unordered_map<Node*, Node*> cacheMap;

    Node* copyRandomList(Node* head) {
        if (head == nullptr) {
            return nullptr;
        }
        Node *cur = head;
        while (cur != nullptr) {
            cacheMap[cur] = new Node(cur->val);
            cur = cur->next;
        }
        cur = head;
        while (cur != nullptr) {
            cacheMap[cur]->next = cacheMap[cur->next];
            cacheMap[cur]->random =  cacheMap[cur->random];
            cur = cur->next;
        }
        return cacheMap[head];
    }
};