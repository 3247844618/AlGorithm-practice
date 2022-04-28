"""逗志芃在干了很多事情后终于闲下来了，然后就陷入了深深的无聊中。
不过他想到了一个游戏来使他更无聊。他拿出n个木棍，然后选出其中一些粘成一根长的，
然后再选一些粘成另一个长的，他想知道在两根一样长的情况下长度最长是多少。
输入格式
　　第一行一个数n，表示n个棍子。第二行n个数，每个数表示一根棍子的长度。
输出格式
　　一个数，最大的长度。
样例输入
4
1 2 3 1
样例输出
3
数据规模和约定
　　n<=15"""
n=int(input())
nums=list(map(int,input().split()))
nums.sort()
def SPlitSubsetSum(nums):
    """01背包 用于判断nums是不是可分为两个等和子集"""
    if len(nums)<2:
        return False
    if sum(nums)%2!=0:
        return False
    target=int(sum(nums)/2)
    """背包容量"""
    dp=[[0]*(target+1) for i in range(len(nums)+1)]
    for i in range(1,len(nums)+1):
        for j in range(1,target+1):
            if j<nums[i-1]:
                dp[i][j]=dp[i-1][j]
            elif j>=nums[i-1]:
                dp[i][j]=max(dp[i-1][j-nums[i-1]]+nums[i-1],dp[i-1][j])
    return dp[len(nums)][target]==target
i=0
while nums:
    if sum(nums[:len(nums)-1])==nums[-1]:
        print(nums[-1])
        break
    while nums[-1]>sum(nums[:len(nums)-1]):
        del nums[-1]
    if SPlitSubsetSum(nums):
        print(int(sum(nums)/2))
        break
    for i in range(len(nums)):
        if sum(nums[i+1:])%2==0:
            del nums[i]
            break
