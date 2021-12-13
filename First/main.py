x = int(input("количество квартир на этаже : "))
y = int(input("первая квартира подезда : "))
z = int(input("квартира № : "))
if y>z:
    print("Неверный ввод")
else:
    floor = (z-y)//x
    if ((z-y)%x)>0:
        floor+=1
    print(floor)