"""问题描述
　　一个8×8的棋盘上有一个马初始位置为(a,b)，他想跳到(c,d)，问是否可以？如果可以，最少要跳几步？
输入格式
　　一行四个数字a,b,c,d。
输出格式
　　如果跳不到，输出-1；否则输出最少跳到的步数。"""
n=int(input())
sx,sy,zx,zy=map(int,input().split())
vis=[[0]*(n+1) for i in range(n+1)]
bs=[[0]*(n+1) for i in range(n+1)]
yd=[[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2]]
vis[sx][sy]=1
dl=[[sx,sy]]
def bfs():
    global dl
    while dl:
        x,y=dl[0]
        if [zx,zy]in dl:
            print(bs[zx][zy])
            return True
        for i in yd:
            tx=x+i[0]
            ty=y+i[1]
            if 0<tx<=n and 0<ty<=n and vis[tx][ty]==0:
                dl.append([tx,ty])
                bs[tx][ty]=bs[x][y]+1
                vis[tx][ty]=1
        del dl[0]
    else:
        return False
if not bfs():
    print(-1)
