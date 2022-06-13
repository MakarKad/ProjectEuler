def dil(m):
    b = 1
    for i in range(1, m + 1):
        if i > m:
            break
        if m % i == 0:
            b += 1
            m = int(m / i)
    return b


b = 0
c = 0
a = 1
while b <= 500:
    b = 0
    c += a
    b = dil(c)
    a += 1
print(b,c)


