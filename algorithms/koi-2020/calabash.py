n, k = map(int, input().split())

bags = [i+1 for i in range(k)]

if sum(bags) > n:
    print(-1)
else:
    n -= sum(bags)
    pos = k-1
    while n > 0:
        bags[pos] += 1
        n -= 1
        pos -= 1
        if pos < 0:
            pos = k-1
    print(bags[-1]-bags[0])