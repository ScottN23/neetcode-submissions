class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        curr = set()
        for n in nums:
            if n in curr:
                return True
            else:
                curr.add(n)
        return False