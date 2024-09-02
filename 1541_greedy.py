####################
####잃어버린 괄호####
####################

line = input()
susik = []
open = False
nocount = True
for i in range(len(line)):
    if nocount == True:
        if line[i] == '0':
            continue
    if line[i] == '-':
        if open == False:
            susik.append(line[i])
            susik.append('(')
            open = True
            nocount = True
            continue
        else:
            susik.append(')')
            susik.append(line[i])
            susik.append('(')
            open = True
            nocount = True
            continue
    elif line[i] == '+':
        susik.append(line[i])
        nocount = True
        continue
    
    susik.append(line[i])
    nocount = False
    if i == len(line)-1:
        if open == True:
            susik.append(')')
# print(susik)
susik=''.join(susik)
# print('susik :', susik)
# print('eval(susik)', eval(susik))
# print('end')
print(eval(susik))