class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumPair = {}
        for i, n in enumerate(nums):
            if target - n in sumPair:
                return [sumPair[target - n], i]
            sumPair[n] = i
        
        