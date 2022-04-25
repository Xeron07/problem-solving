import math


def sum(li1,li2):
    lenOfL1 = len(li1)
    lenOfL2 = len(li2)
    maxLen= max(lenOfL1,lenOfL2)
    fLi=[]
    carry=0
    for i in range(0,maxLen):
        sum = 0
        if lenOfL1>0:
            sum+=li1[lenOfL1-1]
            lenOfL1-=1
        if lenOfL2>0:
            sum+=li2[lenOfL2-1]
            lenOfL2-=1
        sum = sum+carry
        carry=0
        if sum >= 10:
            fLi.append(math.floor(sum%10))
            carry=math.floor(sum/10)
        else:
            fLi.append(sum)
    if carry>0:
        fLi.append(carry)
    return fLi


print(sum([9,9,9,9,9,9,9],[9,9,9,9]))
