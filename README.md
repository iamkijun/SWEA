# SWEA

<<<<<<< Updated upstream
# SWEA

=======
>>>>>>> Stashed changes
## 1959
```
T = int(input())

for k in range(T):
    N, M = map(int, input().split())

    n = list(map(int, input().split()))
    m = list(map(int, input().split()))

    
    max = 0
    

    
    if N<M:
        a = M-N
        for j in range(0,a+1):
            sum = 0
            new = 0
            for i in range(N):
                sum = n[i]*m[i+j]
                new += sum
            if new > max:
                    max = new    

            
            
                

    elif N>M:
        a = N-M
        for j in range(0,a+1):
            sum = 0
            new = 0
            for i in range(M):
                sum = n[i+j]*m[i]
                new += sum
            if new > max:
                    max = new    
            
            
            

    print("#%d %d"%(k+1,max))

```

## 1946

```
T = int(input())

l = [[]]

for i in range(T):
    n = int(input())
	
    print("#%d"%(i+1))

    for j in range(n):

        a, b = map(str, input().split())
        b = int(b)

        for k in range(b):
            l[-1].append(a)
            if len(l[-1]) == 10:
                l.append([])
    
    s = ""

    
    for m in range(len(l)):
        for n in range(len(l[m])):
                s = s + l[m][n]
        print(s)
        s = ""

    l = [[]]
```

## 2063

```
N = int(input())

a = map(int, input().split())
a = list(a)

a.sort(reverse = False)

num = N // 2
print(a[num])
```

## 2058

```
N = int(input())

four = N//1000
three = (N//100)%10
two = (N//10)%10
one = N%10
print(one+two+three+four)
```

## 1936

```
a, b = map(int, input().split())

if a == 1:
    if b == 2:
        print("B")
    elif b == 3:
        print("A")
elif a == 2:
    if b == 1:
        print("A")
    elif b == 3:
        print("B")
elif a == 3:
    if b == 1:
        print("B")
    elif b == 2:
        print("A")
```

## 1989

```
n = int(input())
for i in range(n):
    a = input()
    re = a[::-1]
    if a == re:
        print("#%d 1"%(i+1))
    elif a != re:
        print("#%d 0"%(i+1))
<<<<<<< Updated upstream
```
=======
```
>>>>>>> Stashed changes

## 2001

```
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
```