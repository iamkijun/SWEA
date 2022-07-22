T = int(input())

for i in range(1, T+1):
    n = input()
    for j in range(10):
        for k in range(10,0,-1):
            if n[j:j+k] == n[j+k:j+2*k]:
                print(f'#{i} {k}')
                break
        
    