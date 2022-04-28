'''问题描述
　　给定一个1～N的排列a[i]，每次将相邻两个数相加，得到新序列，再对新序列重复这样的操作，显然每次得到的序列都比上一次的序列长度少1，最终只剩一个数字。
　　例如:
　　3 1 2 4
　　4 3 6
　　7 9
　　16
   (这里等于第n排与对应乘积之和)
　　现在如果知道N和最后得到的数字sum，请求出最初序列a[i]，为1～N的一个排列。若有多种答案，则输出字典序最小的那一个。数据保证有解。
输入格式
　　第1行为两个正整数n，sum
输出格式
　　一个1～N的一个排列'''
def YHSJ(n):
    """用于返回第n行的杨辉三角序数"""
    a=[[0]*n for i in range(n)]
    for i in range(n):
        for j in range(i+1):
            if j==0:
                a[i][j]=1
            elif j==i:
                a[i][j]=1
            else:
                a[i][j]=a[i-1][j]+a[i-1][j-1]
    return a[n-1]


n,SUM=map(int,input().split())
vis=[0]*n
nums=[0]*n
yh_xs=YHSJ(n)
def dfs(step,s):
    if s>SUM:
        return False
    if step==n:
        if s==SUM:
            print(' '.join(str(i)for i in nums))
            return True
        else:
            return False
    for i in range(1,n+1):
        if vis[i-1]==0:
            vis[i-1]=1
            nums[step]=i
            if dfs(step+1,s+i*yh_xs[step]):
                return True
            vis[i-1]=0
    return False

dfs(0,0)
