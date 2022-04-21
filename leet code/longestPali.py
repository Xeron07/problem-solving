def longestPalindrome(s):
    map = {}
    maxL = 0
    maxStr=s[0]
    l = len(s)
    paliCheck = lambda a: a==a[::-1]
    for i in range(0, l):
        print(map)
        if s[i] in map.keys():
            if paliCheck(s[map[s[i]]:i + 1]) and maxL < len(s[map[s[i]]:i + 1]):
                maxStr = s[map[s[i]]:i + 1]
                maxL = len(s[map[s[i]]:i + 1])
        else:
            map[s[i]]= i
    return maxStr


print(longestPalindrome("ccc"))