class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        min_buy = prices[0]
        profit = 0

        for price in prices:
            min_buy = min(min_buy,  price)
            if price > min_buy + fee:
                profit += price - min_buy - fee
                min_buy = price - fee   # key point: 재계산해도 이전에 지불한 fee를 무시

        return profit