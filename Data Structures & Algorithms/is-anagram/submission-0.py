class Solution:
    def countS(self, st: str) -> dict:
        chardic = {}
        for c in st:
            if c not in chardic:
                chardic[c] = 0
            else:
                chardic[c] += 1
        return chardic

    def isAnagram(self, s: str, t: str) -> bool:
        return self.countS(s) == self.countS(t)
        