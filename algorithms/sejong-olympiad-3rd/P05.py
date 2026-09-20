n = int(input())
cur_pass = input()
correct_pass = input()

change_cnt = 0
for i in range(n):
    cnt = abs(int(cur_pass[i]) - int(correct_pass[i]))
    if cnt > 5:
        cnt = 10 - cnt
    change_cnt += cnt

print(change_cnt)
