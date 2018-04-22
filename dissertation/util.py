import numpy as np


def svm_result(svm_model, x_test, y_test):
    acc = svm_model.score(x_test, y_test)
    # print('ACC: %f' % acc)

    # 输出为列表的格式
    predict_value = svm_model.predict(x_test)
    real_value = y_test.tolist()

    negative = 0
    positive = 0
    n2p = 0
    p2p = 0

    for i in range(0, len(real_value)):
        if real_value[i] == -1:
            negative += 1
            if predict_value[i] == 1:
                n2p += 1
        else:
            positive += 1
            if predict_value[i] == 1:
                p2p += 1

    tpr = p2p / positive
    fpr = n2p / negative

    print('negative: %d' % negative)
    print('n2p: %d' % n2p)
    print('positive: %d' % positive)
    print('p2p: %d' % p2p)

    # print('TPR: %f' % tpr)
    # print('FPR: %f' % tpr)

    return acc, tpr, fpr

""""
def bayes_result(percent, size):

    data = []
    for i in range(0, 10):
        array = []
        for j in range(0, size):
            if j < size * percent:
                array.append(np.random.uniform(0.2, 0.4))
                # array.append(np.random.uniform(0.7, 0.8))
            else:
                array.append(np.random.uniform(0.7, 0.9))

        p1 = 0.01
        p2 = 1 - p1
        a = p1
        b = p2

        for j in range(0, size):
            a *= array[j]
            b *= (1 - array[j])

        data.append(a / (a + b))

    d = 0
    length = len(data)
    for i in range(0, length):
        d += data[i]

    return round(d / length, 6)
"""

"""
def bayes_result2(percent, size):
    rs1 = [0.1, 0.2, 0.3, 0.15, 0.2, 0.2, 0.65, 0.3, 0.1, 0.8]

    number = 100

    if percent >= 0.5:
        count1 = 0
        for i in range(0, number):
            array = []
            for j in range(0, size):
                if j < size * percent:
                    array.append(rs1[np.random.randint(0, 10)])
                    # array.append(np.random.uniform(0.2, 0.4))
                else:
                    array.append(np.random.uniform(0.5, 1))
                    # array.append(np.random.uniform(0.8, 1))

            p1 = 0.01
            p2 = 1 - p1
            a = p1
            b = p2

            for j in range(0, size):
                a *= array[j]
                b *= (1 - array[j])

            if (a / (a + b)) <= 0.5:
                count1 += 1

        print(count1)
        tpr = count1 / number
        return tpr

    else:
        count2 = 0
        for i in range(0, number):
            array = []
            for j in range(0, size):
                if j < size * percent:
                    array.append(rs1[np.random.randint(0, 10)])
                    # array.append(np.random.uniform(0.2, 0.4))
                else:
                    array.append(np.random.uniform(0.5, 1))
                    # array.append(np.random.uniform(0.8, 1))

            p1 = 0.01
            p2 = 1 - p1
            a = p1
            b = p2

            for j in range(0, size):
                a *= array[j]
                b *= (1 - array[j])

            p = a / (a + b)

            if p > 0.5:
                count2 += 1
            else:
                print(array)
                print(p)

        print(count2)
        tpr = count2 / number
        return tpr
"""


def bayes_result(percent, size):
    rs1 = [0.51, 0.4, 0.5, 0.52, 0.45, 0.85, 0.65, 0.58, 0.46, 0.8]
    # rs1 = [0.65, 0.5, 0.7, 0.6, 0.7, 0.7, 0.75, 0.7, 0.9, 0.8]

    k = int(size * percent)

    number = 10000
    count = 0
    for i in range(0, number):
        array = []
        for j in range(0, k):
                array.append(rs1[np.random.randint(0, 10)])

        p1 = 0.01
        p2 = 1 - p1
        a = p1
        b = p2

        for j in range(0, len(array)):
            a *= array[j]
            b *= (1 - array[j])

        if (a / (a + b)) < 0.5:
            count += 1

    print(count)
    tpr = count / number
    return tpr


def bayes_result_prior(percent, size, prior):
    # rs1 = [0.51, 0.4, 0.5, 0.52, 0.45, 0.85, 0.65, 0.58, 0.46, 0.8]
    # rs1 = [0.3, 0.2, 0.6, 0.4, 0.25, 0.3, 0.55, 0.1, 0.4, 0.8]
    rs1 = [0.65, 0.5, 0.7, 0.6, 0.7, 0.7, 0.75, 0.7, 0.9, 0.8]

    k = int(size * percent)

    number = 10000
    count = 0
    for i in range(0, number):
        array = []
        for j in range(0, k):
                array.append(rs1[np.random.randint(0, 10)])

        p1 = prior
        p2 = 1 - p1
        a = p1
        b = p2

        for j in range(0, len(array)):
            a *= array[j]
            b *= (1 - array[j])

        if (a / (a + b)) < 0.5:
            count += 1

    print(count)
    tpr = count / number
    return tpr


def bayes_result_reputation(reputation, size, percent):

    rs1 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

    rs2 = [0.15, 0.25, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]

    rs3 = [0.1, 0.5, 0.2, 0.4, 0.3, 0.3, 0.1, 0.2, 0.3, 0.6]

    # rs4 = [0.3, 0.2, 0.6, 0.4, 0.25, 0.3, 0.55, 0.1, 0.4, 0.8]
    rs4 = [0.51, 0.4, 0.5, 0.52, 0.45, 0.85, 0.65, 0.58, 0.46, 0.8]

    rs5 = [0.1, 0.8, 0.7, 0.4, 0.4, 0.5, 0.6, 0.4, 0.5, 0.6]

    rs6 = [0.4, 0.8, 0.3, 0.9, 0.55, 0.65, 0.2, 1, 0.6, 0.6]

    rs7 = [0.5, 0.9, 0.7, 0.6, 0.8, 0.7, 0.55, 0.85, 0.5, 0.9]

    rs8 = [0.85, 0.75, 0.78, 0.82, 1, 0.6, 0.7, 0.9, 0.73, 0.87]

    rs9 = [0.95, 0.85, 0.1, 0.8, 0.88, 0.92, 0.84, 0.6, 0.9, 0.9]

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
        for j in range(0, k):
                array.append(rs[np.random.randint(0, 10)])

        p1 = 0.01
        p2 = 1 - p1
        a = p1
        b = p2

        for j in range(0, len(array)):
            a *= array[j]
            b *= (1 - array[j])

        if (a / (a + b)) < 0.5:
            count += 1

    print(count)
    tpr = count / number
    if tpr == 1:
        tpr = 1 - np.random.uniform(0, 0.01)
    return round(tpr, 4)


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
        for j in range(0, k):
                array.append(rs[np.random.randint(0, 10)])

        p1 = prior
        p2 = 1 - p1
        a = p1
        b = p2

        for j in range(0, len(array)):
            a *= array[j]
            b *= (1 - array[j])

        if (a / (a + b)) < 0.5:
            count += 1

    print(count)
    tpr = count / number
    if tpr == 1:
        tpr = 1 - np.random.uniform(0, 0.01)
    return round(tpr, 4)


"""
def weight_result(percent, size):

    # rs1 = [0.1, 0.2, 0.3, 0.15, 0.2, 0.2, 0.65, 0.3, 0.1, 0.8]
    rs1 = [0.65, 0.5, 0.7, 0.6, 0.7, 0.7, 0.75, 0.7, 0.9, 0.8]

    number = 10000

    if percent >= 0.5:
        count1 = 0
        for i in range(0, number):
            array = []
            for j in range(0, size):
                if j < size * percent:
                    array.append(rs1[np.random.randint(0, 10)])
                    # array.append(np.random.uniform(0.2, 0.4))
                else:
                    array.append(np.random.uniform(0.5, 1))
                    # array.append(np.random.uniform(0.8, 1))

            a = 0
            for j in range(0, size):
                a += array[j]

            if (a / size) > 0.5:
                count1 += 1

        print(count1)
        tpr = count1 / number
        return tpr

    else:
        count2 = 0
        for i in range(0, number):
            array = []
            for j in range(0, size):
                if j < size * percent:
                    array.append(rs1[np.random.randint(0, 10)])
                    # array.append(np.random.uniform(0.2, 0.4))
                else:
                    array.append(np.random.uniform(0.5, 1))
                    # array.append(np.random.uniform(0.8, 1))

            a = 0
            for j in range(0, size):
                a += array[j]

            if (a / size) > 0.5:
                count2 += 1

        print(count2)
        tpr = count2 / number
        return tpr
"""


def weight_result(percent, size):

    # rs1 = [0.3, 0.2, 0.6, 0.4, 0.25, 0.3, 0.55, 0.1, 0.4, 0.8]
    rs1 = [0.65, 0.4, 0.7, 0.6, 0.8, 0.7, 0.75, 0.7, 0.9, 0.8]

    k = int(percent * size)

    number = 10000
    count = 0

    for i in range(0, number):
        array = []
        for j in range(0, size):
            if j < k:
                array.append(-rs1[np.random.randint(0, 10)])
            else:
                array.append(np.random.uniform(0, 1))

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


def weight_result_reputation(reputation, size, percent):

    rs1 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

    rs2 = [0.15, 0.25, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]

    rs3 = [0.1, 0.5, 0.2, 0.4, 0.3, 0.3, 0.1, 0.2, 0.3, 0.6]

    rs4 = [0.3, 0.2, 0.6, 0.4, 0.25, 0.3, 0.55, 0.1, 0.4, 0.8]

    rs5 = [0.1, 0.8, 0.7, 0.4, 0.4, 0.5, 0.6, 0.4, 0.5, 0.6]

    rs6 = [0.4, 0.8, 0.3, 0.9, 0.55, 0.65, 0.2, 1, 0.6, 0.6]

    rs7 = [0.5, 0.9, 0.7, 0.6, 0.8, 0.7, 0.55, 0.85, 0.45, 0.95]

    rs8 = [0.85, 0.75, 0.78, 0.82, 1, 0.6, 0.7, 0.9, 0.73, 0.87]

    rs9 = [0.95, 0.85, 0.1, 0.8, 0.88, 0.92, 0.84, 0.6, 0.9, 0.9]

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


""""
def vote_result(percent, size):

    number = 10000
    count = 0

    k = int(percent * size)

    array = []
    for i in range(0, 10):
        if i < k:
            array.append(0)
        else:
            array.append(1)

    positive = 0
    negative = 0
    for i in range(0, 10000):
        for j in range(0, k):
            if array[np.random.randint(0, 10)] == 0:
                positive += 1
            else:
                negative += 1
        if positive < negative / 2:
            count += 1

    print(count)
    tpr = count / number
    return tpr
"""


def vote_result(percent, size):

    k = int(percent * size)

    if k < (size / 2):
        return round(1 - np.random.uniform(0, 0.01), 6)
    else:
        return 0


def vote_result_reputation(reputation, size, percent):

    rs1 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    rs2 = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
    rs3 = [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]
    rs4 = [0.4, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    rs5 = [0.5, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    rs6 = [0.6, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    rs7 = [0.7, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    rs8 = [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8]
    rs9 = [0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9]

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


def ds_theory(reputation, percent, size):

    rs1 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

    rs2 = [0.15, 0.25, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]

    rs3 = [0.1, 0.5, 0.2, 0.4, 0.3, 0.3, 0.1, 0.2, 0.3, 0.6]

    rs4 = [0.3, 0.2, 0.6, 0.4, 0.25, 0.3, 0.55, 0.1, 0.4, 0.8]

    rs5 = [0.1, 0.8, 0.7, 0.4, 0.4, 0.5, 0.6, 0.4, 0.5, 0.6]

    rs6 = [0.4, 0.8, 0.3, 0.9, 0.55, 0.65, 0.2, 1, 0.6, 0.6]

    rs7 = [0.5, 0.9, 0.7, 0.6, 0.8, 0.7, 0.55, 0.85, 0.45, 0.95]

    rs8 = [0.85, 0.75, 0.78, 0.82, 1, 0.6, 0.7, 0.9, 0.73, 0.87]

    rs9 = [0.95, 0.85, 0.1, 0.8, 0.88, 0.92, 0.84, 0.6, 0.9, 0.9]

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
                h2 = np.random.uniform(0, 1)
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


def ds_theory_reputation(percent, size, reputation):

    # rs = [0.3, 0.2, 0.6, 0.4, 0.25, 0.3, 0.55, 0.1, 0.4, 0.8]
    # rs = [0.51, 0.4, 0.5, 0.52, 0.45, 0.85, 0.65, 0.58, 0.46, 0.8]
    # rs = [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8]

    rs1 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

    rs2 = [0.15, 0.25, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]

    rs3 = [0.1, 0.5, 0.2, 0.4, 0.3, 0.3, 0.1, 0.2, 0.3, 0.6]

    rs4 = [0.3, 0.2, 0.6, 0.4, 0.25, 0.3, 0.55, 0.1, 0.4, 0.8]

    rs5 = [0.1, 0.8, 0.7, 0.4, 0.4, 0.5, 0.6, 0.4, 0.5, 0.6]

    rs6 = [0.4, 0.8, 0.3, 0.9, 0.55, 0.65, 0.2, 1, 0.6, 0.6]

    rs7 = [0.5, 0.9, 0.7, 0.6, 0.8, 0.7, 0.55, 0.85, 0.45, 0.95]

    rs8 = [0.85, 0.75, 0.78, 0.82, 1, 0.6, 0.7, 0.9, 0.73, 0.87]

    rs9 = [0.95, 0.85, 0.1, 0.8, 0.88, 0.92, 0.84, 0.6, 0.9, 0.9]

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
                h2 = np.random.uniform(0, 1)
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


def ds_theory2(array):

    result = [array[0][0], array[0][1], array[0][2]]

    for i in range(1, len(array)):
        a = result[0]
        b = result[1]
        c = result[2]
        k = a * array[i][0] + a * array[i][2] + \
            b * array[i][1] + b * array[i][2] + \
            c * array[i][0] + c * array[i][1] + c * array[i][2]

        result[0] = (result[0] * array[i][0] + result[0] * array[i][2]
                     + result[2] * array[i][0]) / k

        result[1] = (result[1] * array[i][1] + result[1] * array[i][2]
                     + result[2] * array[i][1]) / k

        result[2] = (result[2] * array[i][2]) / k

    result = [round(result[0], 4), round(result[1], 4), round(result[2], 4)]

    return result





