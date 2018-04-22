from dissertation import util

size = 10
percents = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
reputations = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

result = []
for i in range(0, 9):
    percent = percents[i]
    reputation = 0.4
    prior = 0.01
    tpr = util.bayes(reputation=reputation, size=size, percent=percent, prior=prior)
    result.append(tpr)
    print('reputation: {}, percent: {} , prior: {}, tpr: {}'
          .format(reputation, percent, prior, tpr))

print(result)

print("************************************")

result = []
for i in range(0, 9):
    percent = percents[i]
    reputation = 0.7
    prior = 0.01
    tpr = util.bayes(reputation=reputation, size=size, percent=percent, prior=prior)
    result.append(tpr)
    print('reputation: {}, percent: {} , prior: {}, tpr: {}'
          .format(reputation, percent, prior, tpr))

print(result)

print("######### 场景3和场景4 ###############")
print("####################################")

result = []
for i in range(0, 9):
    percent = 0.3
    reputation = reputations[i]
    prior = 0.01
    tpr = util.bayes(reputation=reputation, size=size, percent=percent, prior=prior)
    result.append(tpr)
    print('reputation: {}, percent: {} , prior: {}, tpr: {}'
          .format(reputation, percent, prior, tpr))

print(result)

print("************************************")

result = []
for i in range(0, 9):
    percent = 0.7
    reputation = reputations[i]
    prior = 0.01
    tpr = util.bayes(reputation=reputation, size=size, percent=percent, prior=prior)
    result.append(tpr)
    print('reputation: {}, percent: {} , prior: {}, tpr: {}'
          .format(reputation, percent, prior, tpr))

print(result)

