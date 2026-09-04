class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numLock = set()
        for c in nums:
            if c in numLock:
                return True
            else:
                numLock.add(c)
        return False
