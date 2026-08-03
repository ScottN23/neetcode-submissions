class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevSum = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevSum:
                return [prevSum[diff], i]
            prevSum[n] = i