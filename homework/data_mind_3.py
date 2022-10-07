# 蒙特卡洛法
import random
import data_mind_2
import math
import time

# s = 4
# n = 1000000
# c = 0
# start3 = time.time()
# while abs(c/n*4 - math.pi) > 0.000001:
#     x = random.uniform(-1, 1)
#     y = random.uniform(-1, 1)
#     if (x ** 2 + y ** 2) <= 1:
#         c += 1
#
# print(c / n * 4)
# end3 = time.time()
# print("蒙特卡洛法的运行时间：", end3 - start3)


# 级数展开
n = 1000000
sum0 = 0
i = 1
start2 = time.time()
while abs(sum0 - math.pi ** 2 / 6) > 0.0000001:
    sum0 += 1 / (i ** 2)
    i += 1

print(data_mind_2.newton(6 * sum0))
end2 = time.time()
print("级数展开1运行时间：", end2 - start2)

# 级数展开2
n = 1000000
sum1 = 0
flag = 1
i = 1
start1 = time.time()
while abs(4 * sum1 - math.pi) > 0.0000001:
    sum1 += flag * 1 / (2 * i - 1)
    flag = -flag
    i += 1

print(sum1 * 4)
end1 = time.time()
print("级数展开2的运行时间：", end1 - start1)

# 级数展开3
i = 0
sum3 = 0
start4 = time.time()
while abs(sum3 - math.pi) > 0.0000001:
    sum3 += 16 * (-1) ** i * (1 / 5) ** (2 * i + 1) / (2 * i + 1) - 4 * (-1) ** i * (1 / 239) ** (2 * i + 1) / (
                2 * i + 1)
    i += 1
end4 = time.time()
print(sum3)
print("级数展开3运行时间为：", end4 - start4)
