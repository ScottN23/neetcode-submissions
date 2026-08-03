from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = defaultdict(int), defaultdict(int)
        
        for i in range(len(s1)):
            s1Count[s1[i]] += 1
            s2Count[s2[i]] += 1

        def matches(s1Count, s2Count):
            for c in s1Count:
                if s1Count[c] != s2Count[c]:
                    return False
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            if matches(s1Count, s2Count):
                return True

            s2Count[s2[r]] += 1
            s2Count[s2[l]] -= 1

            if s2Count[s2[l]] == 0:
                del s2Count[s2[l]]
            l += 1
        
        return matches(s1Count, s2Count)
