def plaidromWord(list):
    for word in list:
        if word == word[::-1]:
            return word
    return ""


print(plaidromWord(["def","ghi"]))