"""给出一个区间的集合，请合并所有重叠的区间。

示例 1:

    输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
    输出: [[1,6],[8,10],[15,18]]
    解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6]."""
points=[]
while True:
    i=list(map(int,input().split()))
    if not i:
        break
    points.append(i)
points.sort()
for i in range(1,len(points)):
    left=points[i-1][0]
    right=points[i][1]
    if points[i][0]<=points[i-1][1]:
        del points[i]
        points[i-1]=[left,right]
print(points)
