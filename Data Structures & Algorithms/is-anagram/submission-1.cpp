class Solution {
public:
    bool isAnagram(string s, string t) {
        int lengthS = s.length();
        if (lengthS != t.length()){
            return false;
        }

        unordered_map<char, int> countS;
        unordered_map<char, int> countT;
        int i = 0;
        for (; i < lengthS; i++){
            countS[s[i]]++;
            countT[t[i]]++;
        }
        return countS == countT;
    }
};
