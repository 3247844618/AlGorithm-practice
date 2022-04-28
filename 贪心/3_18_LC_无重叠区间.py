"""力扣题目链接：https://leetcode-cn.com/problems/non-overlapping-intervals

给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

可以认为区间的终点总是大于它的起点。区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。

示例 1:

    输入: [ [1,2], [2,3], [3,4], [1,3] ]
    输出: 1
    解释: 移除 [1,3] 后，剩下的区间没有重叠。"""
nums=[]
while True:
    i=list(map(int,input().split()))
    if not i:
        break
    nums.append(i)
nums.sort()
count=1
for i in range(1,len(nums)):
    if nums[i][0]>=nums[i-1][1]:
        count+=1
    else:
        nums[i][1]=min(nums[i][1],nums[i-1][1])
print(len(nums)-count)
