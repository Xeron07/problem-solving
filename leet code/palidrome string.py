def plaidromWord(list):
    for word in list:
        flag=True
        for i in range(0,len(word)):
            if word[i] != word[-(i+1)]:
                flag = False
                break
        if flag: return word
    return ""


print(plaidromWord(["abc","car","ada","racecar","cool"]))