#####################
######약수 구하기######
#####################
import sys

# n, k = map(int, input().split())
firstData = sys.stdin.readline()
firstData.strip()
a, b = firstData.split(' ')
a= int(a)
b= int(b)
yaksu = []
for i in range(1,a+1):
    if a % i == 0:
        yaksu.append(i)
if len(yaksu)<b:
    result = 0
else:
    result = yaksu[b-1]
print(result)