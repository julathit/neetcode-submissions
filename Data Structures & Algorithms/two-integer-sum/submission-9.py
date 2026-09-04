class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valMap = {}
        for i in range(len(nums)):
            if target-nums[i] not in valMap:
                valMap[target-nums[i]] = [i]
            else:
                valMap[target-nums[i]].append(i)
        for i in range(len(nums)):
            if (nums[i] in valMap):
                for j in valMap[nums[i]]:
                    if i != j:
                        return [i,j]
        return []