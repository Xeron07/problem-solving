strI = input("Enter your String: ")

def maxSubStr(str):
    start=0
    maxLength=0
    map = {}
    if len(str)<=1: return len(str)
    for end in range(0,len(str)):
        if str[end] in map.keys():
            start =max(map.get(str[end]) +1,start)
            map[str[end]]=end
        else:
            map.update({str[end]:end})
        maxLength = max((end - start)+1, maxLength)
    return maxLength



def secondApproach(str):
    start=0
    map={}
    maxLength=0
    for end in range(0,len(str)):
        if str[end] in map.keys():
            start = max(map[str[end]]+1,start)
            map[str[end]]=end
        else:
            map[str[end]]=end
        maxLength = max((end - start) + 1, maxLength)
    return maxLength

print(secondApproach(strI))