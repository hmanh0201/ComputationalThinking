import sys

def main():
    t, m = map(int, sys.stdin.readline().split())

    memory = [0] * m
    id = 1

    for _ in range(t):
        input_data = sys.stdin.readline().strip().split()
        type = input_data[0]

        if type == 'alloc':
            n = int(input_data[1])
            check = False
            for i in range(m):
                canSave = True
                for j in range(i, i + n):
                    if j >= m or memory[j] != 0:
                        canSave = False
                        break
                if canSave:
                    for j in range(i, i + n):
                        memory[j] = id
                    print(id)
                    id += 1
                    check = True
                    break
            if not check:
                print('NULL')

        elif type == 'erase':
            n = int(input_data[1])
            if n <= 0 or n >= id:
                print('ILLEGAL_ERASE_ARGUMENT')
            else:
                found = False
                for i in range(m):
                    if memory[i] == n:
                        memory[i] = 0
                        found = True
                if not found:
                    print('ILLEGAL_ERASE_ARGUMENT')

        elif type == 'defragment':
            new_memory = [0] * m
            index = 0
            for i in range(m):
                if memory[i] != 0:
                    new_memory[index] = memory[i]
                    index += 1
            memory = new_memory

if __name__ == "__main__":
    main()