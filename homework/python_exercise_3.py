s = input("请输入一个字符串：")
slow, fast, start, end = 0, 0, 0, 0
max_len = 0
n = len(s)
while fast <= n:
    if fast == n or s[slow] != s[fast]:
        if max_len < fast - slow:
            max_len = fast - slow
            start = slow
            end = fast
        slow = fast
    fast += 1
print(s[start: end])


