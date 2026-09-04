class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        water = 0

        while i < j:
            if height[i] <= height[j]:
                maxnum = height[i]
                i += 1

                while i < j and height[i] < maxnum:
                    water += maxnum - height[i]
                    i += 1

            else:
                maxnum = height[j]
                j -= 1

                while i < j and height[j] < maxnum:
                    water += maxnum - height[j]
                    j -= 1

        return water

                