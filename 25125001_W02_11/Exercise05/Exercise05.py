import sys

def main():
    input_data = sys.stdin.read().splitlines()

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
        else:
            for i in range(1, len(str)):
                if str[i] == ':':
                    res += (len(str) - i - 1) * current_person
    print(res)

if __name__ == "__main__":
    main()