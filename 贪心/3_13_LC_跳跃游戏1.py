"""给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:

    输入: [2,3,1,1,4]
    输出: true
    解释: 我们可以先跳 1 步，从位置 0 到达 位置 1,
    然后再从位置 1 跳 3 步到达最后一个位置。"""
nums=list(map(int,input().split()))
i=0
j=0
while i<len(nums):
    j=max(nums[i]+i,j)
    if j>=len(nums):
        print("ture")
        break
    elif nums[i]==0 and j==i:
        print("false")
        break
    i+=1
