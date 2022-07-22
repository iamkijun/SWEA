T = int(input())

for i in range(1, T+1):
    a = list(map(int, input().split()))
    max = a[0]
    for i in range(len(a)):
        if a[i] > max