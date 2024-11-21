# Kullanıcıdan bir sayı al
num = int(input("Bir sayı giriniz: "))
# Giriş sayısını sakla
temp = num
# Basamak sayısını bul
n = len(str(num))
# Armstrong hesaplaması için değişken
sum = 0

# Sayının Armstrong sayısı olup olmadığını kontrol et
while temp > 0:
   digit = temp % 10
   sum += digit ** n
   temp //= 10

# Sonucu yazdır
if num == sum:
    print(f"{num}, bir Armstrong sayısıdır.")
else:
    print(f"{num}, bir Armstrong sayısı değildir.")
