n, k, m = map(int, input().split())
if m >= k:
    if (abs(m - k) - 1) <= (n - m) + (k - 1):
        print(abs(m - k) - 1)
    else:
        print((n - m) + (k - 1))
else:
    if (abs(m - k) - 1) <= (n - k) + (m - 1):
        print(abs(m - k) - 1)
    else:
        print((n - k) + (m - 1))
