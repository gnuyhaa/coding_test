T = int(input())
for test_case in range(1, T + 1):
    a, b= map(int, input().split())
    if a > 9 or b > 9:
        print('#%d %d' %(test_case, -1))
    else:
        print('#%d %d' %(test_case, a*b))
