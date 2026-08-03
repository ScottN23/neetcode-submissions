class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        resS, resT = defaultdict(int), defaultdict(int)
        i = 0
        while i < len(s):
            resS[s[i]] += 1
            resT[t[i]] += 1
            i += 1
        return resS == resT

