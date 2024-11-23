import sys

total = 0
for _ in range(5):
    A,B = map(str, input().split())
    aH, aM = A.split(':')
    bH, bM = B.split(':')

    total += ((int(bH) - int(aH)) * 60) + (int(bM) - int(aM))

print(total)
