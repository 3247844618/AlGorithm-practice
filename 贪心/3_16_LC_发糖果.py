"""老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，
老师会根据每个孩子的表现，预先给他们评分。

你需要按照以下要求，帮助老师给这些孩子分发糖果：

    每个孩子至少分配到 1 个糖果。
    相邻的孩子中，评分高(相同都不发)的孩子必须获得更多的糖果。

那么这样下来，老师至少需要准备多少颗糖果呢？
示例 1:

    输入: [1,0,2]
    输出: 5
    解释: 你可以分别给这三个孩子分发 2、1、2 颗糖果。"""
nums=list(map(int,input().split()))
n=len(nums)
for i in range(n-1):
    if nums[i]==nums[i+1]:
        continue
    n+=1
print(n)
