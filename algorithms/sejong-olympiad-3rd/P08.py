n = int(input())
# dist = [[999] * (n+1)] * (n+1)
dist = [[n+1 for j in range(n+1)] for i in range(n+1)]

# print(dist)

for i in range(n-1):
    a, b = map(int,input().split())
    dist[a][b] = 1
    dist[b][a] = 1
    # print(dist)

max_d = 1
isDone = True
while isDone:
    isDone = True
    for i in range(1, n):
        for j in range(i+1, n + 1):
            d = n+1
            if dist[i][j] == n+1:
                for k in range(1, n+1):
                    if k != i and k!= j and dist[i][k] != -1 and dist[j][k] != -1:
                        d = min(d,dist[i][k] + dist[j][k])
            if d != n+1:
                dist[i][j] = d
                dist[j][i] = d
                max_d = max(d, max_d)
            if dist[i][j] == n+1:
                isDone = False

print(max_d)
