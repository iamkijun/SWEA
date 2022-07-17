T = int(input())
li =[]

for i in range(T):
    print(&quot;%d&quot;%(i+1))
    n = int(input())
    for j in range(n):
        s = list(map(int, input().split()))
        li.append(s)
    for k in range(n):
        for l in range(n):
            print(li[k][s])
            print(li[s][k])

print(li)