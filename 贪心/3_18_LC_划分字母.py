"""字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，
同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。

示例：

输入：S = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：划分结果为 "ababcbaca", "defegde", "hijhklij"。每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。"""
s=input()
"各个字母出现的最后一个位置"
Hash=[0]*26
for i in range(len(s)):
    Hash[ord(s[i])-ord('a')]=i
right=0
left=0
result=[]
for i in range(len(s)):
    right=max(right,Hash[ord(s[i])-ord('a')])
    if i==right:
        result.append(right-left+1)
        left=i+1
print(result)
