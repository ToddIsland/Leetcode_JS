class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minVal = float("inf")

        for p in prices:
            res = max(res, p - minVal)
            minVal = min(minVal, p)

        return res
