
n = int(input())
ai = list(map(int,input().split()))
# print(ai)
Ai = list(map(int,input().split()))
# print(Ai)
total=0
for i in range(n):
    total += ai[i]*Ai[i]
print(total)


# print(ai[0]*Ai[0])