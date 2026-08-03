class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        lowest_price = prices[0]
        for price in prices:
            if price < lowest_price:
                lowest_price = price
            max_prof = max(max_prof, price - lowest_price)
        return max_prof