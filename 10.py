parol = int(input())

if 0 < (parol // 1000) < 10:
    if parol // 1000 != parol % 10 and parol // 1000 != (parol // 10) % 10 and parol // 1000 != (parol // 100) % 10 and \
            (parol // 100) % 10 != (parol // 10) % 10 and (parol // 100) % 10 != parol % 10 and (parol // 10) % 10 != \
            parol % 10:
        if 1900 <= parol <= 2050:
            print("ERROR")
        else:
            print("YES")
    else:
        print("ERROR")
else:
    print("ERROR")