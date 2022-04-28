"""在柠檬水摊上，每一杯柠檬水的售价为 5 美元。

顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。

每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。

你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。

注意，一开始你手头没有任何零钱。

如果你能给每位顾客正确找零，返回 true ，否则返回 false 。

示例 1：

    输入：[5,5,5,10,20]
    输出：true"""
nums=list(map(int,input().split()))
shi=[]
wu=[]
es=[]
for i in nums:
    if i==5:
        wu.append(i)
    elif i==10:
        if len(wu)>=1:
            wu.pop()
            shi.append(i)
        else:
            print(False)
            break
    else:
        if len(wu)>=1 and  len(shi)>=1:
            wu.pop()
            shi.pop()
            es.append(i)
            "5万能所以优先用一个10一个5"
        elif len(wu)>=3:
            wu.pop()
            wu.pop()
            wu.pop()
            es.append(i)
        else:
            print(False)
            break
else:
    print(True)
