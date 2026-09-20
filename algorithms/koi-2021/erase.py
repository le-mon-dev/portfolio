n = int(input())
a = [i for i in range(1, n+1)]
last = n
while last > 1:
    for i in range(int(last/2)):
        a[i]= a[i*2+1]
    last = int(last/2)
print(a[0])