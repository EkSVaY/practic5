mass_kg = (float(input("Введите вес в фунтах: ")) * 0.4535)
height_cm = (float(input("Введите рост в дюймах: ")) * 2.54)
imt = mass_kg / ((height_cm / 100) ** 2)

if imt < 16:
    print("выраженный дефицит массы тела")
elif 16 <= imt < 18.5:
    print("Недостаточная масса тела")
elif 18.5 <= imt < 25:
    print("норма")
elif 25 <= imt < 30:
    print("избыточная масса тела")
elif 30 <= imt < 35:
    print("Ожирение первой степени")
elif 35 <= imt < 40:
    print("Ожирение второй степени")
else:
    print("Ожирение третьей степени")
