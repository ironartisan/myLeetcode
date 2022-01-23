class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char, int> m;
        for (auto & c : s) {
            m[c]++;
        }
        auto cmp = [](pair<char, int> &a, pair<char, int> &b)
        {
            return a.second <= b.second;
        };

        priority_queue<pair<char, int>, vector<pair<char, int>>, decltype(cmp)> heap(cmp);

        for (auto &i : m) {
            heap.push(i);
        }
        string res;

        while (!heap.empty()) {
            res += string(heap.top().second, heap.top().first);
            heap.pop();
        }
        return res;
    }
};