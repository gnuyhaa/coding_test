import sys
N = int(input())

lowest_y = None

for i in range(N):
    x, y = map(int, input().split())

    if lowest_y is None or y < lowest_y:
        lowest_y = y
        lowest_x = x
print(lowest_x, lowest_y)
