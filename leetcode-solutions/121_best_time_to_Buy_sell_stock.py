class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof = 0 # set profit to be initially zero
        cheapest = prices[0] # the initial cheapest is just the first index

        for p in prices: 
            if p < cheapest: # check each iteration if something is cheaper
                cheapest = p
            if (p - cheapest) > maxprof: # if the current - cheapest is greater than previous max profit, update maxprofit
                maxprof = p - cheapest
            
        return maxprof
    
