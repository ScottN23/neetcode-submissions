class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        countTrack = []
        for num, freq in count.items():
            heapq.heappush(countTrack, (-1 * freq, num))

        res = []
        for i in range(k):
            res.append(heapq.heappop(countTrack)[1])

        return res

        