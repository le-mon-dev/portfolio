n = int(input())

cnt = 0
for m4 in range(int(n/4)+1):
    for m3 in range(int(n/3)+1):
        for m2 in range(int(n/2)+1):
            if m4*4 + m3*3 + m2*2 == n:
                cnt += 1
            # print(m4, m3, m2)
print(cnt)
