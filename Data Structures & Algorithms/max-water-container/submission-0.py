class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        area_max = 0
        while l < r:
            area_max = max(area_max, (r - l) * min(heights[l], heights[r]))
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] <= heights[l]:
                r -= 1
        return area_max

