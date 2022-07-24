T = int(input())

for k in range(1,T+1):
    
    N = input()
    c = 2
    count = 1
    l = []

    for i in range(len(N)):
        a = int(N[i])
        l.append(a)

    while True:
        new = int(N) * c

        for j in range(len(str(new))):
            a = str(new)[j]
            a = int(a)
            l.append(a)

        c += 1
        count += 1
        
        check_list = list(set(l))
        
        if check_list == [0,1,2,3,4,5,6,7,8,9]:
            break
        
        
    print(f'#{k} {count}')