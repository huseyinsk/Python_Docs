#Soru 11: Asal sayılar, yalnızca 1 ve kendisi ile tam olarak bölünebilen pozitif tam sayılardır.
#Şimdi sizden, kullanıcının girdiği bir sayının asal olup olmadığını kontrol eden
#ve sonucu ekrana yazdıran bir Python programı yazmanızı istiyoruz
x = int(input("Bir sayı giriniz: "))
y = []
z = 1
sayac = 0
while z <= x:
    if x % z == 0:
        y.append(z)
        sayac += 1
    z += 1
if sayac == 2 :
    print(f"{x} sayısı bir asal sayıdır.")
else:
    print(f"{x} sayısı bir asal sayı değildir.")
    print("Bölen sayılar: ", y)

#Soru 11: Asal sayılar, yalnızca 1 ve kendisi ile tam olarak bölünebilen pozitif tam sayılardır.
#Şimdi sizden, kullanıcının girdiği bir sayının asal olup olmadığını kontrol eden
#ve sonucu ekrana yazdıran bir Python programı yazmanızı istiyoruz
