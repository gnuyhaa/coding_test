T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    total = 0
    for i in range(1,n+1):
        if i % 2 == 0:
            total -= i
        else: 
            total += i
    print(f"#{test_case} {total}")
