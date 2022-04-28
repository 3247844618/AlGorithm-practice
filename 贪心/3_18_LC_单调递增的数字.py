"""给定一个非负整数 N，找出小于或等于 N 的最大的整数，
同时这个整数需要满足其各个位数上的数字是单调递增。

（当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。）

示例 1:

    输入: N = 10
    输出: 9"""
n=list(map(int,input()))
if len(n)==1:
    print(n[0])
else:
    for i in range(len(n)-1,0,-1):
        while True:
            if n[i]>=n[i-1]:
                break
            else:
                n[i-1]-=1
                n[i]=9
    for i in range(len(n)):
        if n[i]:
            print(n[i],end="")
