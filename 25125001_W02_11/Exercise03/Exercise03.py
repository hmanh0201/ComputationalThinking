import sys

def main():
    s = input()
    t = input()
    xS = ord(s[0]) - ord('a') + 1
    xT = ord(t[0]) - ord('a') + 1
    yS = 9 - int(s[1])
    yT = 9 - int(t[1])

    res = 0
    ans = []

    while xS != xT or yS != yT:
        moveX = xT - xS
        moveY = yT - yS

        strX = ""
        strY = ""
        if moveX > 0:
            strX = "R"
            xS += 1
        elif moveX < 0:
            strX = "L"
            xS -= 1
        if moveY > 0:
            strY = "D"
            yS += 1
        elif moveY < 0:
            strY = "U"
            yS -= 1
        ans.append(strX + strY)
        res += 1

    print(res)
    for str in ans:
        print(str)

if __name__ == "__main__":
    main()