class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maps = {}
        for i in nums:
            if i not in maps:
                maps[i] = 0
            else:
                maps[i] += 1
        return sorted(maps, key=maps.get,reverse = True)[0:k]