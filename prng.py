def lcg(a, c, m, x0, n):
    results = []
    x = x0
    for i in range(n):
        x = (a * x + c) % m
        results.append(x)
    return results

def bbs(p, q, x0, n):
    results = []
    x = x0
    for i in range(n):
        x = (x**2) % (p*q)
        results.append(x)
    return results
output = lcg(1664525, 1013904223, 2**32, 1, 10)
for i in output:
    print(i)
print("#-------------------")
output = bbs(11, 23, 3, 10)
for i in output:
    print(i)