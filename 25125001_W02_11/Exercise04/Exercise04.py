import sys

def main():
    w = int(input())
    if w % 2 == 0 and w != 2:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()