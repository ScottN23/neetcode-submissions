class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Manually count the frequency of each element using a dictionary
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        
        # Step 2: Build a max-heap (negative frequency to simulate max-heap)
        max_heap = [(-freq, num) for num, freq in freq_map.items()]
        heapq.heapify(max_heap)
        
        # Step 3: Extract the top k elements
        result = []
        for _ in range(k):
            result.append(heapq.heappop(max_heap)[1])
        
        return result

        