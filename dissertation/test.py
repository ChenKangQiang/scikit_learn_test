import numpy as np

# 0,1,2,3
s_type = np.random.randint(0, 4)
e_type = np.random.randint(0, 4)
# 最大速度为16.7 m/s
s_speed = round(np.random.randint(0, 17) + np.random.random(), 2)

s_acc = round(np.random.randint(-5, 3) + np.random.random(), 2)
d1 = round(np.random.randint(20, 1200) + np.random.random(), 2)
d2 = round(np.random.randint(20, 1200) + np.random.random(), 2)
rs = round(np.random.random(), 2)

b = np.random.randint(0, 2)
f_type = np.random.randint(0, 3)
rf = round(np.random.random(), 2)

# 单跳
if b == 0:
    f_type = s_type
    rf = rs

result = -1

if s_speed > 14:
    result = 1

if d1 > 1000:
    result = 1

if b == 0 and d2 > 1000:
    result = 1

if s_acc > 2:
    result = 1

if rs < 0.4:
    result = 1

if rf < 0.3:
    result = 1

data = (s_type, e_type, s_speed, s_acc, d1, d2, rs, b, f_type, rf, result)


print("s_type: %d " % s_type)
print("e_type: %d " % e_type)
print("s_speed: %f " % s_speed)
print("s_acc: %f" % s_acc)
print("d1: %f" % d1)
print("d2: %f" % d2)
print("rs: %f" % rs)

print("b: %d" % b)
print("f_type: %d" % f_type)
print("rf: %f" % rf)

print("result: %d" % result)

print(data)


