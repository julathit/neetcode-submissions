class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> seen;

        for (int i = 0; i < nums.size(); i++) {
            int need = target - nums[i];

            if (seen.find(need) != seen.end()) {
                return {seen[need]+1, i+1};
            }

            seen[nums[i]] = i;
        }

        return {};
    }
};