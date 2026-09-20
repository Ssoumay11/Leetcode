class Solution {
public:
    string minWindow(string s, string t) {
        int n = s.length();
        map<char, int> mp;
        
        for(char &ch : t) { // map me store kr lete hai
            mp[ch]++;
        }
        
        int requiredCount = t.length();
        int i = 0, j  = 0;
        int minStart  = 0;
        int minWindow = INT_MAX;

        while(j < n) {
            char ch_j = s[j];
            if(mp[ch_j] > 0)  // like A
                requiredCount--;
            
            mp[ch_j]--; // map -- krnege 
            
            while(requiredCount == 0) { // shrink the window
                if(minWindow > j-i+1) {
                    minWindow = j-i+1;
                    minStart  = i;
                }
                
                char ch_i = s[i];
                mp[ch_i]++; // shink ho rha hai // element add ho rha hai jo freq jo min hui hai 
                if(mp[ch_i] > 0)
                    requiredCount++;
                i++;
            }
            
            j++; //remeber
        }
        
        return minWindow == INT_MAX ? "" : s.substr(minStart, minWindow);
    }
};
