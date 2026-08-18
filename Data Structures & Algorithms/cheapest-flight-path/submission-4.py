class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for i in range(k + 1):
            tempPrices = prices.copy()
            for from_i, to_i, price_i in flights:
                if price_i + prices[from_i] < tempPrices[to_i]:
                    tempPrices[to_i] = price_i + prices[from_i]
            prices = tempPrices
        
        if prices[dst] == float('inf'):
            return -1
        return prices[dst]
                