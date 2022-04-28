"""给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:
    输入: [7,1,5,3,6,4]
    输出: 7
    解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出,
    这笔交易所能获得利润 = 5-1 = 4。随后，在第 4 天（股票价格 = 3）的时候买入，
    在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3
同一天可以卖出在买入"""
nums=list(map(int,input().split()))
def maxProfit(prices):
    result = 0
    for i in range(1, len(prices)):
        result += max(prices[i] - prices[i - 1], 0)
    return result
"""取交易利润为正的"""
print(maxProfit(nums))


"dp"
"0表示买(或不买)后持有的现金 1表示卖(或不卖)后的现金"
dp=[[0]*2 for i in range(len(nums))]
for i in range(len(nums)):
    if i==0:
        dp[i][0]-=nums[i]
        continue
    dp[i][0]=max(dp[i-1][1]-nums[i],dp[i-1][0])
    dp[i][1]=max(dp[i-1][0]+nums[i],dp[i][1])
print(max(dp[len(nums)-1][0],dp[len(nums)-1][1]))
