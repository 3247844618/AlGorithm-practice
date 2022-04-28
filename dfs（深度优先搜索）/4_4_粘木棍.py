"""　有N根木棍，需要将其粘贴成M个长木棍，使得最长的和最短的的差距最小。
输入格式
　　第一行两个整数N,M。
　　一行N个整数，表示木棍的长度。
输出格式
　　一行一个整数，表示最小的差距
数据规模和约定
　　N, M<=7
"""
n,m=map(int,input().split())
nums=list(map(int,input().split()))
nums.sort()
ws=[nums.pop() for i in range(m)]
ws.sort()
while nums:
    ws[0]+=nums.pop()
    ws.sort()
print(max(ws)-min(ws))
