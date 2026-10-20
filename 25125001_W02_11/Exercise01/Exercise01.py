n, m, c = map(int, input().split())
n = (n + c - 1) // c
m = (m + c - 1) // c
print(m * n)