"""问题描述
　　在一个n*n的棋盘中，每个格子中至多放置一个车，
且要保证任何两个车都不能相互攻击，有多少中放法(车与车之间是没有差别的)
输入格式
　　包含一个正整数n
输出格式
　　一个整数，表示放置车的方法数
数据规模和约定
　　n<=8
　　【样例解释】一个车都不放为1种，放置一个车有4种，放置2个车有2种。
"""
n=int(input())
count=0
y=[0]*n

def dfs(step):
    global count
    if step==n:
        count+=1
        return
    for j in range(n):
        if not y[j]:
            y[j]=1
            dfs(step+1)
            y[j]=0
    dfs(step+1)
dfs(0)
print(count)
