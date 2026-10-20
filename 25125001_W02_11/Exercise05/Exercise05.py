import sys

def main():
    input_data = sys.stdin.read().splitlines()

    for i in input_data:
        print(i)
    return

    current_person = 0
    idx = 0
    res = 0

    for line in input_data:
        str = input_data[idx]
        idx += 1
        if str[0] == '+':
            current_person += 1
        elif str[0] == '-':
            current_person -= 1
        for i in range(1, len(str)):
            if str[i] == ':':
                res += len(str) - i 
    print(res)

if __name__ == "__main__":
    main()