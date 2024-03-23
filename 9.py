n, k, m = map(int, input().split())

if n >= m >= k:
    print(n, m, k)
elif n >= k >= m:
    print(n, k, m)
elif m >= n >= k:
    print(m, n, k)
elif m >= k >= n:
    print(m, k, n)
elif k >= m >= n:
    print(k, m, n)
elif k >= n >= m:
    print(k, n, m)
else:
    print(m, n, k)