###################
#####동전 문제######
###################
import sys


firstData = sys.stdin.readline()
firstData.strip()
a, b = firstData.split(' ')
a= int(a)
b= int(b)


lines = []
for i in range(a):
    line = int(input())
    lines.append(line)
Num = 0
for i in range(a):
    coin = lines.pop()
    if b>=coin:
        Num = Num + b//coin
        b = b%coin
        if b==0:
            break

print(Num)