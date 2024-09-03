#####################
######회의실 배정######
#####################
import sys


N = int(input())
time_list  = []
for i in range(N):
    each_time = input()
    start, end = each_time.split(' ')
    start = int(start)
    end = int(end)
    time_list.append((start, end))
time_list.sort()
Num_list = []

for j in range(N):
    Num = 1
    for i in range(N):
        if Num == 1:
            a, b = time_list[j]
        if j+i == N-1:
            break
        c, d = time_list[j+i+1]
        if b <= c :
            a, b = time_list[j+i+1]
            Num += 1
    Num_list.append(Num)
answer = max(Num_list)
print(answer)
# print('answer : ', answer)

# print('time_list : ', time_list)

    



'''
예제
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
'''