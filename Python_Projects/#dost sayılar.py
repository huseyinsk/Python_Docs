def carpanlar_toplami(sayi):
    toplam = 0
    for i in range(1, sayi):
        if sayi % i == 0:
            toplam += i
    return toplam
x = int(input("X sayısını giriniz: "))
y = int(input("Y sayısını giriniz: "))
x_toplam = carpanlar_toplami(x)
y_toplam = carpanlar_toplami(y)

if x_toplam == y and y_toplam == x:
    print(f"{x} ve {y} dost sayılardır.")
else:
    print(f"{x} ve {y} dost sayılar değildir.")