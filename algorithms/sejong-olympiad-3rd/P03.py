a, b = map(int,input().split())
A, B = map(int,input().split())
if a*A + b*B >= 10000:
    print(a*A + b*B - 1000)
else:print(a*A + b*B)