'共有n种图案的印章，每种图案的出现概率相同。小A买了m张印章，求小A集齐n种印章的概率。'
'一行两个正整数n和m'
'输出格式  一个实数P表示答案，保留4位小数。'
n,m=map(int ,input().split())
dp=[[0]*(m+1) for i in range(n+1)]  'n为行,m为列,dp[i][j]表示买j张只中i种的概率'
p=1/n
for i in range(1,n):
    for j in  range(1,m):
        if j<i:
            dp[i][j]=0
        elif i==1:
            if j==1
            
            dp[i][j]=p**(j-1)
        else:
            dp[i][j]=dp[i][j-1]*i*p+dp[i-1][j-1]*(n-i+1)
print('{:.4f}'.format(dp[n][m]))
