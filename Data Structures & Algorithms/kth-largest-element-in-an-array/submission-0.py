class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for n in nums:
            maxHeap.append(-1 * n)
        heapq.heapify(maxHeap)
        while k > 1:
            heapq.heappop(maxHeap)
            k -= 1
        return heapq.heappop(maxHeap) * -1