class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for string in strs:
            currTracker = [0] * 26
            for c in string:
                currTracker[ord(c) - ord('a')] += 1
            res[tuple(currTracker)].append(string)
        
        return list(res.values())