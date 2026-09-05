
class Solution {
public:
    int n;

    //  reference pass kro  → no copy
    bool isPalindrome(int l, int r, const string &s) {
        while (l < r) {
            if (s[l] != s[r]) return false;
            l++;
            r--;
        }
        return true;
    }

    void solve(vector<vector<string>> &result, vector<string> &temp, const string &s, int idx) {
        if (idx == n) {
            result.push_back(temp);
            return;
        }

        for (int i = idx; i < n; i++) {
            if (isPalindrome(idx, i, s)) {
                temp.push_back(s.substr(idx, i - idx + 1)); // add substring
                solve(result, temp, s, i + 1);                 // recurse
                temp.pop_back();                            // backtrack
            }
        }
    }

    vector<vector<string>> partition(string s) {
        n = s.length();
        vector<vector<string>> result;
        vector<string> temp;
        solve(result, temp, s, 0);
        return result;
    }
};
