n = int(input())

gal = int((n / 29) / 17)
sik = int((n / 29) - gal * 17)
knat = n - gal * 17 * 29 - sik * 29

if sik == 0 and gal == 0 and knat == 0:
    print("Денег нет, но вы держитесь!")
elif sik == 0 and gal == 0:
    print(knat, "кнатов")
elif sik == 0 and knat == 0:
    print(gal, "галлеонов")
elif gal == 0 and knat == 0:
    print(sik, "сиклей")
elif gal == 0:
    print(sik, "сиклей")
    print(knat, "кнатов")
elif sik == 0:
    print(gal, "галлеонов")
    print(knat, "кнатов")
elif knat == 0:
    print(gal, "галлеонов")
    print(sik, "сиклей")
else:
    print(gal, "галлеонов")
    print(sik, "сиклей")
    print(knat, "кнатов")
