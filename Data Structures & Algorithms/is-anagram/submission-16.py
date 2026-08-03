class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        resS = defaultdict(int)
        resT = defaultdict(int)
        i = 0
        while i < len(s):
            resS[s[i]] += 1
            resT[t[i]] += 1
            i += 1
        if resS == resT:
            return True
        else:
            return False

