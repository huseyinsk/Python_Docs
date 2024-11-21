#Bir sayıyı başka bir sayıya bölme işlemini, çıkarma işlemleri ile yazınız
#For ve while ile yazılacak.

a = int(input("Bölünen sayıyı giriniz: "))
b = int(input("Bölen sayıyı giriniz: "))
c = a
sayac = 0
while c >= b:
    c -= b
    sayac += 1

print("kalan: ", c, " bölüm: ", sayac)

-------------------------------------

a = int(input("Bölünen sayıyı giriniz: "))
b = int(input("Bölen sayıyı giriniz: "))
c = a
sayac = 0
for i in range(a):
    if c < b:
        break
    c -= b
    sayac += 1

print("Kalan: ", c, ", Bölüm: ", sayac)
