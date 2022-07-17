T = int(input())

sum = 0
max =0
li = []

for i in range(T):
    a, b = map(int, input().split())
    for j in range(a):
        c = list(map(int, input().split()))
        li.append(c)

    for k in range(a-b+1):
        for l in range(b):
            for m in range(b):
                sum += li[k+m][k+l]

        if sum > max:
            max = sum

        sum = 0
        

    print("#%d %d"%(i+1,max))
    sum = 0
    max = 0
    li = []