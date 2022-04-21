# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
# log10(n) returns the length of n digit-1
import math

x = int(input("Enter Number: "))
lenx = math.floor(math.log10(x))
print(lenx)

xaxis = x
yaxis = x
flag = True


def returnFloorNum(n):
    return math.floor(n)


for i in range(0, int(lenx / 2)):
    a = returnFloorNum(xaxis / 10 ** (lenx - i))
    b = returnFloorNum(yaxis % 10)
    xaxis = returnFloorNum(xaxis % 10 ** (lenx - i))
    yaxis = returnFloorNum(yaxis / 10)
    if (a != b):
        print("not")
        flag = False
        break
if (flag):
    print("It Is")


def secondApproach(num):
    strNum = str(x)
    if (num % 2 == 0):
        if strNum[0:(int(num / 2) + 1)][::-1] == strNum[-((int(num / 2) + 1)):]:
            print("it is")
        else:
            print("not1")
    else:
        if (strNum[0:int(num / 2)][::-1] == strNum[(int(num / 2) + 1):]):
            print("it is")
        else:
            print("not")


secondApproach(lenx + 1)


def checkPan(n):
    lenOfx = math.floor(math.log10(n))
    fromLeft = fromRight = n
    for i in range(0, lenOfx):
        a = fromLeft / 10 ** (lenOfx - i)
        b = fromRight % 10
        if a != b: return False

        fromLeft = fromLeft % 10 ** (lenOfx - i)
        fromRight = fromRight / 10
    return True


print(checkPan(x))
