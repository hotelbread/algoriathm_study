#####################
########이진수########
#####################
"""
문제 :
양의 정수 n이 주어졌을 때, 이를 이진수로 나타냈을 때 1의 위치를 모두 찾는 프로그램을 작성하시오. 최하위 비트(least significant bit, lsb)의 위치는 0이다.

입력:
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, n이 주어진다. (1 ≤ T ≤ 10, 1 ≤ n ≤ 10^6)

출력:
각 테스트 케이스에 대해서, 1의 위치를 공백으로 구분해서 줄 하나에 출력한다. 위치가 낮은 것부터 출력한다.


"""

a= int(input()) # 테스트케이스
# print(f'a : {a}, b: {b}')
while a>0:
    b= int(input()) # n 정수
    result = []
    index = 0
    answer = ''
    while b>0:
        if b % 2 == 1:
            result.append(index)
            index +=1
            b = b//2
        else:
            index +=1
            b = b/2
    for i in result:
        if answer =='':
            answer += str(i)
            continue
        answer += ' ' + str(i)
    print(answer)
    a -= 1