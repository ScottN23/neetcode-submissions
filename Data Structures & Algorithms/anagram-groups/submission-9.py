from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaTrack = defaultdict(list)
        for s in strs:
            cCount = [0] * 26
            for c in s:
                cCount[ord(c) - ord('a')] += 1
            anaTrack[tuple(cCount)].append(s)
        
        return list(anaTrack.values())