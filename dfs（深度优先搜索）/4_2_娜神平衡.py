"""琦琦给了娜娜一些两两不等的数，希望娜娜能把这些数分成两组A和B，满足以下条件：
　　1：每一次只能操作一个数，即只取出一个数分入A中或B中；
　　2：每一次操作完成后，A中数之和与B中数之和的差不能超过r。
　　新时代的丘比特们啊，帮帮娜娜吧！
样例输入
4 10
9 6 4 20
样例输出
4 6 9
20
样例说明
　　先把4和6先后分入A组，再把20分入B组，最后把9分入A组。
数据规模和约定
　　很小，真的很小。
"""
n,r=map(int,input().split())
nums=list(map(int,input().split()))
frist=nums[0]
vis=[0]*n
def dfs(a,b,nums):
    if abs(sum(a)-sum(b))>r:
        return False
    if len(a)+len(b)-2==len(nums):
        a.pop(0)
        b.pop(0)
        a.sort()
        b.sort()
        if frist in b:
            a,b=b,a
        print(' '.join(list(map(str,a))))
        print(' '.join(list(map(str,b))))
        return True
    for i in range(len(nums)):
        if vis[i]==0:
            vis[i]=1
            if dfs(a+nums[i:i+1],b,nums):
                return True
            elif dfs(a,b+nums[i:i+1],nums):
                return True
            vis[i]=0
    return False


dfs([0],[0],nums)
