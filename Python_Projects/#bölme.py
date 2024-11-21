
bölünen = int(input("Bölünen sayiyi giriniz: "))
bölen = int(input("Bölen sayiyi giriniz: "))
bölüm = 0  # Bölme işleminin sonucu
kalan = bölünen  # Her çıkarma işleminden sonra kalan miktar
# For döngüsü kullanarak çıkarma işlemlerini gerçekleştirelim
for _ in range(bölen):
    if kalan >= bölen:
        kalan -= bölen  # Kalanı güncelle
        bölüm += 1  # Bölüm sayısını artır
    else:
        break  # Eğer kalan, bölen'den küçükse döngüyü sonlandır
#################
# Bölünen, bölen'den büyük veya eşit olduğu sürece döngüyü çalıştır
while kalan >= bölen:
    kalan -= bölen  # Kalanı güncelle
    bölüm += 1  # Bölüm sayısını artır