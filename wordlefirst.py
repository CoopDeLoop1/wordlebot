import random
import time
words = open('wordlewords.txt','r')
fixed = words.readlines()
length = 5
results = []
ranks = open('wordlestartsranked.txt', 'w')
for i in words.readlines():
    if len(i) == length+1:
        fixed.append(i)
words = fixed.copy()
def test(guess,target):
    ans = ''
    for i in range(length):
        if guess[i] == target[i]:
            ans = ans + '2'
        elif guess[i] in target:
            ans = ans + '1'
        else:
            ans = ans + '0'
    return [guess,ans]
def possible(fixed,failed,somewhere,sure):
    newwords = []
    for i in range(len(fixed)):
        flag = True
        for j in failed:
            if j in fixed[i] and flag:
                flag = False
        if flag:
            for j in range(len(somewhere)):
                if (((not somewhere[j][0] in fixed[i]) or (fixed[i][somewhere[j][1]] == somewhere[j][0])) and flag):
                    flag = False
        if flag:
            for j in range(len(sure)):
                if not sure[j][0] == fixed[i][sure[j][1]]:
                    flag = False
        if flag:
            newwords.append(fixed[i])
    return(newwords)
averages = []
iter = 0
for n in words:
    if iter > -1: 
        values = []
        for k in fixed:
            failed = []
            somewhere = []
            sure = []
            testresults = test(n,k)
            for j in range(length):
                if testresults[1][j] == '0':
                    failed.append(testresults[0][j])
                elif testresults[1][j] == '1':
                    somewhere.append([testresults[0][j],j])
                elif testresults[1][j] == '2':
                    sure.append([testresults[0][j],j])
            values.append(len(possible(fixed,failed,somewhere,sure)))
        averages.append(sum(values)/(len(values)))
        ranks.write(str(n[0:length]) + '\n')
        ranks.write(str(averages[-1]) + '\n')
        print(n[0:length])
        print(averages[-1])
        print('\n')
    iter += 1
guess = words[averages.index(min(averages))]
print(min(averages))
print(guess)
words.close()
