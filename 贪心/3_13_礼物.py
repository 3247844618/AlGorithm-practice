"""题描述
　　JiaoShou看到了排成一排的N个石子。
　　这些石子很漂亮，JiaoShou决定以此为礼物。
　　但是这N个石子被施加了一种特殊的魔法。
　　如果要取走石子，必须按照以下的规则去取。
　　每次必须取连续的2*K个石子，并且满足前K个石子的重量和小于等于S，后K个石子的重量和小于等于S。
　　由于时间紧迫，Jiaoshou只能取一次。
　　现在JiaoShou找到了聪明的你，问他最多可以带走多少个石子。
输入格式
　　第一行两个整数N、S。
　　第二行N个整数，用空格隔开，表示每个石子的重量。"""
n,S = list(map(int,input().split()))

a = list(map(int,input().split()))

f = [0]*n
g = [0]*n

# 预处理f
i = 0
j = 0
Sum = a[0]

while i<=j and j<n:
        if Sum > S:
                Sum -= a[i]
                i += 1
        else:
             f[j] = j-i+1
             j += 1
             if j==n: break
             Sum += a[j]

# 预处理g
i = n-1
j = n-1
Sum = a[n-1]

while i>=j and j>=0:
        if Sum > S:
                Sum -= a[i]
                i -= 1
        else:
             g[j] = i-j+1
             j -= 1
             if j<0: break
             Sum += a[j]
# 求解
print(max([min(f[i],g[i+1]) for i in range(n-1)])*2)

        

