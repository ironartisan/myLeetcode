
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};


class Solution {
public:
    unordered_map<Node *, Node *> visited;
    Node* cloneGraph(Node* node) {
        
        if (node == nullptr) {
            return node;
        }

        if (visited.find(node) != visited.end()) { // node已经被访问过，直接取回对应的克隆节点
            return visited[node];
        }
        
        Node* cloneNode = new Node(node->val); // 克隆节点
        visited[node] = cloneNode; // 哈希表存储

        for(auto& neighbor: node->neighbors) {  // 遍历该节点的邻居并更新克隆节点的邻居列表
            cloneNode->neighbors.emplace_back(cloneGraph(neighbor));
        }
        return cloneNode;
    }
};