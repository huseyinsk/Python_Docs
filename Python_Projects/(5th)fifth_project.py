#bir sayıyı başka bir say ile çarpma işlemini, toplama işlemleri kullanarak
#gerçekleştiren bir python programını while ve sonra for ile yazınız.

a = int(input("Birinci çarpan sayıyı giriniz: "))
b = int(input("İkinci çarpan sayıyı giriniz: "))
sayac = 0
toplam = 0
while sayac < b:
    toplam += a
    sayac += 1
print("Çarpım: ", toplam)


----------------------------------
x = int(input("Birinci çarpan sayıyı giriniz: "))
y = int(input("İkinci çarpan sayıyı giriniz: "))
toplam = 0
for i in range(y):
    toplam += x
print("Çarpım: ", toplam)
