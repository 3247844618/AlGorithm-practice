"""问题描述
　　给出一个正整数n，求一个和最大的序列a0，a1，a2，……，ap，满足n=a0>a1>a2>……>ap且ai+1是ai的约数，输出a1+a2+……+ap的最大值
输入格式
　　输入仅一行，包含一个正整数n
输出格式
　　一个正整数，表示最大的序列和，即a1+a2+……+ap的最大值
样例输入
10
样例输出
6
数据规模和约定
　　1<n<=10^6"""
n=int(input())
div=n
SUM=0
while n!=1:
    if n%div==0 and n>div:
        n=div
        SUM+=n
    div-=1
print(SUM)
