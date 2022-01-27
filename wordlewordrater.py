import random
words = open('wordlewords.txt','r')
fixed = []
length = 5
results = []
fixed = words.readlines()
words = fixed.copy()
target = input('answer\n')

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
iter = 0
while True:
    print('possible words left: ' + str(len(fixed)))
    guess = input('word\n')
    result = test(guess, target)
    results.append(result)
    values = []
    for k in fixed:
        failed = []
        somewhere = []
        sure = []
        testresults = test(guess,k)
        for j in range(length):
            if testresults[1][j] == '0':
                failed.append(testresults[0][j])
            elif testresults[1][j] == '1':
                somewhere.append([testresults[0][j],j])
            elif testresults[1][j] == '2':
                sure.append([testresults[0][j],j])
        values.append(len(possible(fixed,failed,somewhere,sure)))
    print("your guess's score: " + str(sum(values)/len(values)))
    if iter > 0:
        averages = []
        for n in words:
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
        flag = False
        newpossible = []
        for i in range(len(fixed)):
            if averages[words.index(fixed[i])] == min(averages):
                newpossible.append(fixed[i])
                flag = True
        if flag:
            guess = random.choice(newpossible)
            print('randomly chosen from: ' + str(newpossible))
        else:
            guess = words[averages.index(min(averages))]
        print('optimal: ' + guess[0:length] + ' at ' + str(min(averages)))
    print(results)
    failed = []
    somewhere = []
    sure = []
    for i in results:
        for j in range(length):
            if i[1][j] == '0':
                failed.append(i[0][j])
            elif i[1][j] == '1':
                somewhere.append([i[0][j],j])
            elif i[1][j] == '2':
                sure.append([i[0][j],j])
    fixed = possible(fixed,failed,somewhere,sure)
    print('remaining: ' + str(len(fixed)) + '\n')
    iter += 1
    if results[-1][1] == '22222':
        break