#Pozitif tam sayılan olan X ve Y için, eğer X sayısının çarpanları(kendisi hariç)
#toplamı Y sayısına ve aynı zamanda Y sayısının çarpanları(kendisi hariç) toplamı
#X sayısına eşitse, bu sayılar dost sayılardır.
X = int(input("Bir X sayısı giriniz : "))
Y = int(input("Bir Y sayısı giriniz : "))
def carpanlar_toplami(X,Y):
    c = 0
    d = 0
    for i in range(1,X):
        if X % int(i) == 0:
            c += i
    for j in range(1,Y):
        if Y % int(j) == 0:
            d += j
    if c == Y and d == X:
        print("Girmiş olduğunuz iki sayı dost sayıdır.")
    else:
        print("Girmiş olduğunuz iki sayı dost sayı değildir.")

carpanlar_toplami(X,Y)
