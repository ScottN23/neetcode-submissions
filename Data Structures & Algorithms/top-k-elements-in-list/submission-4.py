from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nCount = Counter(nums)
        topK = []
        for n, o in nCount.items():
            if len(topK) < k: 
                heapq.heappush(topK, (o, n))
            elif topK[0][0] < o:
                heapq.heappop(topK)
                heapq.heappush(topK, (o, n))

        ans = []
        for o, n in topK:
            ans.append(n)

        return ans