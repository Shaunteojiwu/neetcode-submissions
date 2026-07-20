class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        #min_max={}
        diff=0

        for right in range(1,len(prices)):
            if prices[left]<=prices[right]:
                diff=max(diff, (prices[right]-prices[left]))
            else:
                left=right
            # if prices[right]<prices[left]:
            #     left=right
            # else:
            #     diff=max(diff,(prices[right]-prices[left]))
        return diff
