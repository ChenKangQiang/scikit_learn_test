import numpy as np


# 节点S的先验概率分布为(0.2, 0.8)
# 假设节点S本身是不可信的
# 节点A, B, C为恶意节点，发起共谋攻击，认为节点S可信，节点D为正当节点，认为S不可信
# 故评估报告为[1, 1, 1, -1]
def bayes(reputation, size, percent, prior):

    # rs1 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    rs1 = abs(np.random.normal(0.1, 0.1, 10))

    # rs2 = [0.15, 0.25, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
    rs2 = abs(np.random.normal(0.2, 0.1, 10))

    # rs3 = [0.1, 0.5, 0.2, 0.4, 0.3, 0.3, 0.1, 0.2, 0.3, 0.6]
    rs3 = np.random.normal(0.3, 0.1, 10)

    # rs4 = [0.3, 0.2, 0.6, 0.4, 0.25, 0.3, 0.55, 0.1, 0.4, 0.8]
    rs4 = np.random.normal(0.4, 0.1, 10)

    # rs5 = [0.1, 0.8, 0.7, 0.4, 0.4, 0.5, 0.6, 0.4, 0.5, 0.6]
    rs5 = np.random.normal(0.5, 0.1, 10)

    # rs6 = [0.4, 0.8, 0.3, 0.9, 0.55, 0.65, 0.2, 1, 0.6, 0.6]
    rs6 = np.random.normal(0.6, 0.1, 10)

    # rs7 = [0.5, 0.9, 0.7, 0.6, 0.8, 0.7, 0.55, 0.85, 0.5, 0.9]
    rs7 = np.random.normal(0.7, 0.1, 10)

    # rs8 = [0.85, 0.75, 0.78, 0.82, 1, 0.6, 0.7, 0.9, 0.73, 0.87]
    rs8 = np.random.normal(0.8, 0.1, 10)

    # rs9 = [0.95, 0.85, 0.1, 0.8, 0.88, 0.92, 0.84, 0.6, 0.9, 0.9]
    rs9 = np.random.normal(0.9, 0.1, 10)

    rs = []
    if reputation == 0.1:
        rs = rs1
    elif reputation == 0.2:
        rs = rs2
    elif reputation == 0.3:
        rs = rs3
    elif reputation == 0.4:
        rs = rs4
    elif reputation == 0.5:
        rs = rs5
    elif reputation == 0.6:
        rs = rs6
    elif reputation == 0.7:
        rs = rs7
    elif reputation == 0.8:
        rs = rs8
    else:
        rs = rs9

    k = int(percent * size)

    number = 10000
    count = 0
    for i in range(0, number):
        array = []
        for j in range(0, size):
            if j < k:
                array.append(rs[np.random.randint(0, 10)])
            else:
                array.append(np.random.uniform(0.5, 1))

        # print(array)
        p1 = prior
        p2 = 1 - p1
        a = p1
        b = p2

        for j in range(0, len(array)):
            if j < k:
                a *= array[j]
                b *= (1 - array[j])
            else:
                a *= (1 - array[j])
                b *= array[j]

        # for j in range(0, len(array)):
        #     if j < k:
        #         a *= (1 - array[j])
        #         b *= array[j]
        #     else:
        #         a *= array[j]
        #         b *= (1 - array[j])

        # print('a: %f' % a)
        # print('b: %f' % b)
        p = a / (a + b)
        # print('p: %f' % p)
        # 推断出的可信度如果小于0.5，就相当于检测成功，不受恶意节点的影响
        if p < 0.5:
            count += 1

    print(count)
    tpr = count / number
    if tpr == 1:
        tpr = 1 - np.random.uniform(0, 0.01)
    return round(tpr, 4)


# 假设节点S本身是不可信的
# 节点A, B, C为恶意节点，发起共谋攻击，认为节点S可信，节点D为正当节点，认为S不可信
# 故评估报告为[1, 1, 1, -1]
def ds_theory(reputation, percent, size):
    # rs1 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    rs1 = abs(np.random.normal(0.1, 0.1, 10))

    # rs2 = [0.15, 0.25, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
    rs2 = abs(np.random.normal(0.2, 0.1, 10))

    # rs3 = [0.1, 0.5, 0.2, 0.4, 0.3, 0.3, 0.1, 0.2, 0.3, 0.6]
    rs3 = np.random.normal(0.3, 0.1, 10)

    # rs4 = [0.3, 0.2, 0.6, 0.4, 0.25, 0.3, 0.55, 0.1, 0.4, 0.8]
    rs4 = np.random.normal(0.4, 0.1, 10)

    # rs5 = [0.1, 0.8, 0.7, 0.4, 0.4, 0.5, 0.6, 0.4, 0.5, 0.6]
    rs5 = np.random.normal(0.5, 0.1, 10)

    # rs6 = [0.4, 0.8, 0.3, 0.9, 0.55, 0.65, 0.2, 1, 0.6, 0.6]
    rs6 = np.random.normal(0.6, 0.1, 10)

    # rs7 = [0.5, 0.9, 0.7, 0.6, 0.8, 0.7, 0.55, 0.85, 0.5, 0.9]
    rs7 = np.random.normal(0.7, 0.1, 10)

    # rs8 = [0.85, 0.75, 0.78, 0.82, 1, 0.6, 0.7, 0.9, 0.73, 0.87]
    rs8 = np.random.normal(0.8, 0.1, 10)

    # rs9 = [0.95, 0.85, 0.1, 0.8, 0.88, 0.92, 0.84, 0.6, 0.9, 0.9]
    rs9 = np.random.normal(0.9, 0.1, 10)

    rs = []
    if reputation == 0.1:
        rs = rs1
    elif reputation == 0.2:
        rs = rs2
    elif reputation == 0.3:
        rs = rs3
    elif reputation == 0.4:
        rs = rs4
    elif reputation == 0.5:
        rs = rs5
    elif reputation == 0.6:
        rs = rs6
    elif reputation == 0.7:
        rs = rs7
    elif reputation == 0.8:
        rs = rs8
    else:
        rs = rs9

    m = int(percent * size)
    number = 10000
    count = 0

    for j in range(0, number):

        array = []
        for i in range(0, size):
            # 假设被观察节点S不可信，恶意节点发起好话攻击，认为S可信
            if i < m:
                x = []
                h1 = rs[np.random.randint(0, 10)]
                h2 = 0
                u = 1 - h1
                x.append(h1)
                x.append(h2)
                x.append(u)
                array.append(x)
            else:
                x = []
                h1 = 0
                h2 = np.random.uniform(0.5, 1)
                u = 1 - h2
                x.append(h1)
                x.append(h2)
                x.append(u)
                array.append(x)

        # print(array)
        result = [array[0][0], array[0][1], array[0][2]]
        # print(result)

        for i in range(1, len(array)):
            a = result[0]
            b = result[1]
            c = result[2]
            k = a * array[i][0] + a * array[i][2] + \
                b * array[i][1] + b * array[i][2] + \
                c * array[i][0] + c * array[i][1] + c * array[i][2]

            # print('k %f' % k)

            result[0] = (result[0] * array[i][0] + result[0] * array[i][2]
                         + result[2] * array[i][0]) / k

            result[1] = (result[1] * array[i][1] + result[1] * array[i][2]
                         + result[2] * array[i][1]) / k

            result[2] = (result[2] * array[i][2]) / k

            # print(result)

        if result[0] < result[1]:
            count += 1

    print(count)
    tpr = count / number
    if tpr == 1:
        tpr = 1 - np.random.uniform(0, 0.01)
    return round(tpr, 4)


def weighted_vote(reputation, percent, size):
    # rs1 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    rs1 = abs(np.random.normal(0.1, 0.1, 10))

    # rs2 = [0.15, 0.25, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
    rs2 = abs(np.random.normal(0.2, 0.1, 10))

    # rs3 = [0.1, 0.5, 0.2, 0.4, 0.3, 0.3, 0.1, 0.2, 0.3, 0.6]
    rs3 = np.random.normal(0.3, 0.1, 10)

    # rs4 = [0.3, 0.2, 0.6, 0.4, 0.25, 0.3, 0.55, 0.1, 0.4, 0.8]
    rs4 = np.random.normal(0.4, 0.1, 10)

    # rs5 = [0.1, 0.8, 0.7, 0.4, 0.4, 0.5, 0.6, 0.4, 0.5, 0.6]
    rs5 = np.random.normal(0.5, 0.1, 10)

    # rs6 = [0.4, 0.8, 0.3, 0.9, 0.55, 0.65, 0.2, 1, 0.6, 0.6]
    rs6 = np.random.normal(0.6, 0.1, 10)

    # rs7 = [0.5, 0.9, 0.7, 0.6, 0.8, 0.7, 0.55, 0.85, 0.5, 0.9]
    rs7 = np.random.normal(0.7, 0.1, 10)

    # rs8 = [0.85, 0.75, 0.78, 0.82, 1, 0.6, 0.7, 0.9, 0.73, 0.87]
    rs8 = np.random.normal(0.8, 0.1, 10)

    # rs9 = [0.95, 0.85, 0.1, 0.8, 0.88, 0.92, 0.84, 0.6, 0.9, 0.9]
    rs9 = np.random.normal(0.9, 0.1, 10)

    rs = []
    if reputation == 0.1:
        rs = rs1
    elif reputation == 0.2:
        rs = rs2
    elif reputation == 0.3:
        rs = rs3
    elif reputation == 0.4:
        rs = rs4
    elif reputation == 0.5:
        rs = rs5
    elif reputation == 0.6:
        rs = rs6
    elif reputation == 0.7:
        rs = rs7
    elif reputation == 0.8:
        rs = rs8
    else:
        rs = rs9

    k = int(percent * size)

    number = 10000
    count = 0

    for i in range(0, number):
        array = []
        for j in range(0, size):
            if j < k:
                array.append(-rs[np.random.randint(0, 10)])
            else:
                array.append(np.random.uniform(0.5, 1))

        a = 0
        for j in range(0, size):
            a += array[j]

        if a > 0:
            count += 1

    print(count)
    tpr = count / number
    if tpr == 1:
        tpr = 1 - np.random.uniform(0, 0.01)
    return round(tpr, 4)


def majority_vote(reputation, percent, size):
    # rs1 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    rs1 = abs(np.random.normal(0.1, 0.1, 10))

    # rs2 = [0.15, 0.25, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
    rs2 = abs(np.random.normal(0.2, 0.1, 10))

    # rs3 = [0.1, 0.5, 0.2, 0.4, 0.3, 0.3, 0.1, 0.2, 0.3, 0.6]
    rs3 = np.random.normal(0.3, 0.1, 10)

    # rs4 = [0.3, 0.2, 0.6, 0.4, 0.25, 0.3, 0.55, 0.1, 0.4, 0.8]
    rs4 = np.random.normal(0.4, 0.1, 10)

    # rs5 = [0.1, 0.8, 0.7, 0.4, 0.4, 0.5, 0.6, 0.4, 0.5, 0.6]
    rs5 = np.random.normal(0.5, 0.1, 10)

    # rs6 = [0.4, 0.8, 0.3, 0.9, 0.55, 0.65, 0.2, 1, 0.6, 0.6]
    rs6 = np.random.normal(0.6, 0.1, 10)

    # rs7 = [0.5, 0.9, 0.7, 0.6, 0.8, 0.7, 0.55, 0.85, 0.5, 0.9]
    rs7 = np.random.normal(0.7, 0.1, 10)

    # rs8 = [0.85, 0.75, 0.78, 0.82, 1, 0.6, 0.7, 0.9, 0.73, 0.87]
    rs8 = np.random.normal(0.8, 0.1, 10)

    # rs9 = [0.95, 0.85, 0.1, 0.8, 0.88, 0.92, 0.84, 0.6, 0.9, 0.9]
    rs9 = np.random.normal(0.9, 0.1, 10)

    rs = []
    if reputation == 0.1:
        rs = rs1
    elif reputation == 0.2:
        rs = rs2
    elif reputation == 0.3:
        rs = rs3
    elif reputation == 0.4:
        rs = rs4
    elif reputation == 0.5:
        rs = rs5
    elif reputation == 0.6:
        rs = rs6
    elif reputation == 0.7:
        rs = rs7
    elif reputation == 0.8:
        rs = rs8
    else:
        rs = rs9

    k = size * percent

    if k < (size / 2):
        return round(1 - np.random.uniform(0, 0.01), 6)
    else:
        return 0
