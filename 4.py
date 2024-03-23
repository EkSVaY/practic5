a = int(input())

if a % 10 == 1 and a // 10 != 1:
    print(a, "попугай")
if a % 10 in [2, 3, 4] and a // 10 != 1:
    print(a, "попугая")
if a // 10 == 1 or a % 10 in [0, 5, 6, 7, 8, 9]:
    print(a, "попугаев")
