'迷宫问题'
'输入n表示，再输入n*n的矩阵用于表示迷宫，1表示墙0表示可以走'
'初始坐标（0,0）终点右下角'
n=int(input())
mg=[[i for i in map(int ,input().split())]for j in range(n)]
yd=[(-1,0),(0,1),(1,0),(0,-1)]
zt=[[0]*n for i in range(n)]
def dfs(x,y):
    if zt[n-1][n-1]==1:
        for i in zt:
            for j in i:
                print(j,end='')
            print()
        print('\n\n')
        return 0
    for i in range(4):
        tx=x+yd[i][0]
        ty=y+yd[i][1]
        if 0<=tx<n and 0<=ty<n and mg[tx][ty]==0 and zt[tx][ty]==0:
            zt[tx][ty]=1
            dfs(tx,ty)
            zt[tx][ty]=0
    zt[x][y]=0
zt[0][0]=1
dfs(0,0)
