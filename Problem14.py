def get_chain(a, b={}, c=0):
    m = a
    while a != 1:
        if a in b:
            c += b[a]
            b[m] = c
            return b
        if a % 2 == 0:
            a = int(a / 2)
        else:
            a = a * 3 + 1
        c += 1
    c += 1
    b[m] = c
    return b


for i in range(1,1000000):
    get_chain(i)

a = get_chain(1)
c = max(a.values())
b = {i[1]:i[0] for i in a.items()}
print(b[c])
