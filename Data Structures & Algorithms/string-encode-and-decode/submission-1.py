class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += s + ":;,"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        curr = ""
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i] == ":" and s[i + 1] == ";" and s[i + 2] == ",":
                res.append(curr)
                curr = ""
                i += 3
            else:
                curr += s[i]
                i += 1
        
        return res
