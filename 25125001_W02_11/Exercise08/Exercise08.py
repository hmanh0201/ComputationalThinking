import sys

def main():
    path = input()
    x = 0
    y = 0

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    d = {}
    d[(0, 0)] = True
    preX = 0
    preY = 0

    for i in range(len(path)):
        if path[i] == 'U':
            y += 1
        elif path[i] == 'D':
            y -= 1
        elif path[i] == 'L':
            x -= 1
        elif path[i] == 'R':
            x += 1  
        if (x, y) in d:
            print("BUG")
            return
        d[(x, y)] = True
        for j in range(4):
            d[(preX + dx[j], preY + dy[j])] = True
            # print(preX + dx[j], preY + dy[j])
        preX = x
        preY = y
    print("OK")
if __name__ == "__main__":
    main()