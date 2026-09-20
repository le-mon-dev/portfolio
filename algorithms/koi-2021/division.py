n = int(input())
a = list(map(int,input().split()))
equals = 0
for i in range(n-3):
    for j in range(i +1, n-2):
        for k in range(j+1, n-1):
            if sum(a[0:i+1]) == sum(a[i+1:j+1]) == sum(a[j+1:k+1]) == sum(a[k+1:n]):
                print(a[0:i+1], a[i+1:j+1], a[j+1:k+1],a[k+1:n])
                equals += 1
print(equals)