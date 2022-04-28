'八皇后'
'输入一个数n,在n*n矩阵，同一行同一列与斜着只能放一个'
n=int(input())
dt=[[0]*n for i in range(n)]
hang=[0]*n
lie=[0]*n
zx=[0]*2*n
yx=[0]*2*n
def dfs(x,cont):
    if x>=n:
        cont+=1
        print(cont)
        for i in dt:
            for j in i:
                print(j,end='')
            print()
        print("\n\n")
        return
    for i in range(n):
        if hang[x]==0 and lie[i]==0 and zx[x+i]==0 and yx[x-i+n]==0:
            dt[x][i]=1
            hang[x]=1
            lie[i]=1
            zx[x+i]=1
            yx[x-i+n]=1
            dfs(x+1,cont)
            dt[x][i]=0
            hang[x]=0
            lie[i]=0
            zx[x+i]=0
            yx[x-i+n]=0

dfs(0,0)
