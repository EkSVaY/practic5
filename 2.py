xc = float(input("xc: "))
yc = float(input("yc: "))
r = float(input("r: "))
x = float(input("x: "))
y = float(input("y: "))

if (x - xc) ** 2 + (y - yc) ** 2 < r**2:
    print("Точка внутри окружности")
elif ((x - xc) ** 2 + (y - yc) ** 2) == r**2:
    print("Лежит на окружности")
else:
    print("Точка вне окружности")
