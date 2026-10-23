import sys

def isGrid(xx, yy, n, m):
    if xx < 0 or yy < 0 or xx >= n or yy >= m:
        return False
    return True

def main():

    n, m, c = input().split()
    n = int(n)
    m = int(m)

    a = []
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    d = {}
    res = 0

    for i in range(n):
        a.append(input())

    for i in range(n):
        for j in range(m):
            if a[i][j] == c[0]:
                # print(i, j)
                for k in range(4):
                    xx = i + dx[k]
                    yy = j + dy[k]
                    if isGrid(xx, yy, n, m):
                        d[a[xx][yy]] = d.get(a[xx][yy], 0) + 1
                        # print(xx, yy, a[xx][yy], d[a[xx][yy]])
                        if d[a[xx][yy]] == 1 and a[xx][yy] != c[0] and a[xx][yy] != '.': 
                            res = res + 1
    print(res)


if __name__ == "__main__":
    main()