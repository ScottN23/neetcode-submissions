class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numTarget = {}
        for i in range(len(nums)):
            if target - nums[i] in numTarget:
                return [numTarget[target - nums[i]], i]
            else:
                numTarget[nums[i]] = i