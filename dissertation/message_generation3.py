import csv
import numpy as np

csvFile = open('message3.csv', 'w')
writer = csv.writer(csvFile)
writer.writerow(['S_type', 'E_type', 'S_speed', 'S_acc', 'D1', 'D2', 'Rs', 'B', 'F_type', 'Rf', 'Result'])

for i in range(1, 10000):
    # 0,1,2,3
    s_type = np.random.randint(0, 4)
    e_type = np.random.randint(0, 4)
    # 最大速度为16.7 m/s
    s_speed = round(np.random.uniform(0, 18), 2)
    # 加速度的范围为 -4.5~2.6
    s_acc = round(np.random.uniform(-5, 3), 2)
    d1 = round(np.random.uniform(20, 1100), 2)
    d2 = round(np.random.uniform(20, 1100), 2)
    rs = round(np.random.uniform(0.2, 1), 2)

    b = np.random.randint(0, 2)
    f_type = np.random.randint(0, 3)
    rf = round(np.random.uniform(0.2, 1), 2)

    # 单跳
    if b == 0:
        f_type = s_type
        rf = rs

    result = -1

    if d1 > 1000 or (b == 0 and d2 > 1000):
        result = 1

    if s_acc > 2.3 or s_speed > 16:
        result = 1

    if rs < 0.3 and rf < 0.3:
        result = 1

    # if b == 0 and d2 > 1000:
    #     result = 1
    #
    # if s_acc > 2:
    #     count += 1
    #
    # if rs < 0.4:
    #     count += 1
    #
    # if rf < 0.3:
    #     count += 1
    #
    # if count >= 3:
    #     result = 1

    data = (s_type, e_type, s_speed, s_acc, d1, d2, rs, b, f_type, rf, result)

    writer.writerow(data)

csvFile.close()
