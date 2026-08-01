class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxele = 0
        currprice = 0
        l,r = 0,1
        while r<len(prices):
            if prices[l]<prices[r]:
                currprice = max(currprice, prices[r]-prices[l])
                r+=1
            else:
                l=r
                r+=1
        return currprice