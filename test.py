temp = input().split('-')

num = []

for i in temp:
    sum = 0
    tmp = i.split('+')
    
    for j in tmp:
        sum += int(j)
        
    num.append(sum)

n = num[0]

for i in range(1,len(num)): 
    n -= num[i]
    
print(n)
#추가함