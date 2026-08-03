class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 1 1 2 3 4
        # ^
        # 1 2 3 4 1
        # ^
        # 2 3 4 1 1
        # ^
        
        l, r = 0, 0
        while r < len(nums):
            if nums[l] == val:
                currIndex = l
                while currIndex < len(nums) - 1:
                    nums[currIndex] = nums[currIndex + 1]
                    currIndex += 1
                r += 1
            else:
                l += 1
                r += 1

        return l
