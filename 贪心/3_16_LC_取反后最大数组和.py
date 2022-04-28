"""给定一个整数数组 A，我们只能用以下方法修改该数组：

我们选择某个索引 i 并将 A[i] 替换为 -A[i]，然后总共重复这个过程 K 次。
（我们可以多次选择同一个索引 i。）以这种方式修改数组后，返回数组可能的最大和。

示例 1：

    输入：A = [4,2,3], K = 1
    输出：5
    解释：选择索引 (1,) ，然后 A 变为 [4,-2,3]。"""
nums=list(map(int,input().split()))
k=int(input())
nums.sort()
x=-1
for i in range(len(nums)-1,-1,-1):
    if nums[i]<0:
        x=i
        break
nums1=nums[:x+1]
nums2=nums[x+1:]
j=0
while k!=0:
    if  nums1==[]:
        nums2[0]*=-1
        k-=1
    else:
        if len(nums1)>=k:
            nums1[j]*=-1
            j+=1
            k-=1
        else:
            if j==len(nums1)-1:
                if nums1[-1]<nums2[0]:
                    nums1[-1]*=-1
                    k-=1
                else:
                    nums2[0]*=-1
                    k-=1
print(sum(nums1+nums2))
