import sys

input_data = sys.stdin.readline().split()

n = int(input_data[0])
data = {}
rounds = []
for _ in range(n):
    name, point = sys.stdin.readline().split()
    point = int(point)
    data[name] = data.get(name, 0) + point
    rounds.append((name, data[name]))
max_point = max(data.values())
for name, current_point in rounds:
    if current_point >= max_point and data[name] == max_point:
        print(name)
        break