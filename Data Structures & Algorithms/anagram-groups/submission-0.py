class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        newst = {}

        for sta in strs:
            com = str(sorted(sta))
            if com in newst:
                newst[com].append(sta)
            else:
                newst[com] = [sta]
        return list(newst.values())