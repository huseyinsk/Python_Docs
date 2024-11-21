#Bir sayı alınız ve armstrongmudur kontrol ediniz
#Armstrong 153, basamak sayısı kadar üssü toplamı aynı sayıyı vercek
#1 + 125 + 27 = 153

sayi = input("Bir sayı giriniz: ")
uzunluk = len(sayi)
toplam = 0
for i in sayi:
    a = int(i) ** uzunluk
    toplam += a
if toplam == int(sayi):
    print("Girmiş olduğunuz sayı bir armstrong sayıdır.")
else:
    print("Girmiş olduğunuz sayı bir armstrong sayı değildir.")
