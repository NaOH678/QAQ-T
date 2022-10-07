# 循环迭代，逐步逼近
def method_1(x):
    i = 1
    while x - i ** 2 >= 0.0001:
        i = i + 0.00001
    return i


# 二分查找
def binary_search(x):
    left, right, ans = 0, x, -1
    while left <= right:
        mid = (left + right) / 2
        if mid * mid <= x:
            ans = mid
            left = mid + 0.0001
        else:
            right = mid - 0.0001
    return ans


# 牛顿法
def newton(c):
    g = c / 2
    i = 0
    while abs(g * g - c) > 0.00000000001:
        g = (g + c / g) / 2
        i = i + 1
    return g
