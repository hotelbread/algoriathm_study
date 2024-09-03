#######################
######설탕배달문제######
#######################

N = int(input()) # 설탕무게를 받음 3=<N=<5000
kg5 = N//5
Num : int = 0
for i in range(kg5, -1, -1):
    if (N - 5*i) % 3 == 0:
        kg3 = (N - 5 * i) //3
        Num = Num + i + kg3
        break
    else:
        continue
if Num == 0:
    Num = -1
print(Num)