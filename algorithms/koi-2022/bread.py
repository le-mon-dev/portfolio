n = int(input())
inf = 10000
ans = inf

for i in range(n):
    a, b = map(int, input().split())
    if a <= b:
        ans = min(ans, b)
if ans == inf:
    print(-1)
else:
    print(ans)


