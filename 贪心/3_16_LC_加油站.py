"""在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。

你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油
cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。

如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。

说明:

    如果题目有解，该答案即为唯一答案。
    输入数组均为非空数组，且长度相同。
    输入数组中的元素均为非负数。

示例 1: 输入:

    gas  = [1,2,3,4,5]
    cost = [3,4,5,1,2]

输出: 3，"""
gas=list(map(int,input().split()))
cost=list(map(int,input().split()))

for i in range(len(gas)):
    Remain_Oil=0
    Remain_Oil+=gas[i]
    if Remain_Oil<cost[i]:
        continue
    else:
        Remain_Oil-=cost[i]
        for j in range(i+1,len(gas)+i+1):
            Remain_Oil+=gas[j%len(gas)]
            Remain_Oil-=cost[j%len(gas)]
            if Remain_Oil<0:
                break
        else:
            print(i)
            break
else:
    print(-1)
