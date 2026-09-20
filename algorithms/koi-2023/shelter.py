n, k = map(int, input().split())
x, y = [0]*n, [0]*n
for i in range(n):
    x[i], y[i] = map(int, input().split())

def max_dist(i, j, k):
    re = 0
    for u in range(n):
        re = max(re, min(abs(x[k]-x[u])+abs(y[k]-y[u]), abs(x[i]-x[u])+ abs(y[i]-y[u]), abs(x[j]-x[u])+abs(y[j]-y[u])))
    return re
ans = 10 ** 9

if k == 1:
    for i in range(n):
        ans = min(ans, max_dist(i, i, i))
elif k == 2:
    for i in range(n):
        for j in range (i, n):
            ans = min(ans, max_dist(i, j, j))
else:
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                ans = min(ans, max_dist(i, j, k))
print(ans)



