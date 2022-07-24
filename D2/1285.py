T = int(input())

for i in range(1,T+1):
    N = int(input())
    a= list(map(int, input().split()))
    min = 1000
    count = 0
    for i in range(len(a)):
        if abs(a[i]) < min:
            min = abs(a[i])
            count = 1
        elif abs(a[i]) == min:
            count += 1
        
    print(f'#{i} {min} {count}')