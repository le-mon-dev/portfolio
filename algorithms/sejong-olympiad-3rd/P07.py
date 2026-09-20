n = int(input())

price = 0
for i in range(n):
    g,s = map(int,input().split())
    if g>=70 and s>=20:
        print('A')
        price += 150000
    elif g>=60 and s>=15:
        print('B')
        price += 100000
    elif g>=50:
        print('C')
        price += 50000
    else:
        print('D')
        price += 200000
print(price)
