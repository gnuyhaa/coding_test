T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    hour = a + b
    print('#%d %d' % (test_case, hour % 24))          
