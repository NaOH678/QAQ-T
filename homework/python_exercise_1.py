muti = 1;
for i in range(1, 100):
    if i % 2 == 1:
        print(i, end=" ")
        if i < 50:
            muti *= i
print(" ")
print("50以内奇数的乘积：", muti)
