"""给定一个整数数组 nums ，找到一个具有最大和的
连续子数组（子数组最少包含一个元素），
返回其最大和。

示例: 输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
"""
nums=list(map(int,input().split()))


"""暴力求解"""
pre=0
for i in range(len(nums)):
    cur=0
    for j in nums[i:]:
        cur+=j
        pre=max(cur,pre)
print(pre)


"""贪心"""
nums=list(map(int,input().split()))
"当前sum"
cur=0
"前一个"
pre=0
for i in range(len(nums)):
    cur+=nums[i]
    "当连续和cur<0后置位0"
    if cur <0:
        cur=0
    "pre 记录最大连续和"
    pre=max(pre,cur)
print(pre)


"""dp"""
dp=[0]*len(nums)
dp[0]=nums[0]
for i in range(1,len(nums)):
    dp[i]=max(dp[i-1]+nums[i],dp[i])
print(max(dp))
