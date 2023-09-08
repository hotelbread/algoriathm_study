###################
#####ATM 문제######
###################

#입력부
N = int(input()) #총 인원
time_list = input() #k번째 수
number_list = time_list.split()
int_list = [int(num) for num in number_list]

int_list.sort()
eachTime = 0
finalTime = 0

for i in int_list:    
    eachTime += i
    finalTime += eachTime

print(finalTime)