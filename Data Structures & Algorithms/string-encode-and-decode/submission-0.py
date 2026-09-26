class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "空"
        return "我".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "空":
            return []
        return s.split("我")