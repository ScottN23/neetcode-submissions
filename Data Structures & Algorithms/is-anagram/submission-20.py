class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sTrack = {}
        for c in s:
            if c in sTrack:
                sTrack[c] += 1
            else:
                sTrack[c] = 1

        tTrack = {}
        for c in t:
            if c in tTrack:
                tTrack[c] += 1
            else:
                tTrack[c] = 1

        return sTrack == tTrack