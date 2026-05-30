class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        max_prof = 0
        while r < len(prices) - 1:
            if prices[l] < prices[r]:
                profit = prices[r]-prices[l]
                max_prof = max(profit, max_prof)
                r += 1
            if prices[r] < prices[l]:
                l = r
                r += 1
            if prices[r] == prices[l]:
                r += 1
        return max_prof