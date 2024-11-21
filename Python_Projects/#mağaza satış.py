# Kullanıcı girdilerini alın
ilk_gun_fiyati = float(input("İlk gün fiyatını giriniz (TL): "))
artis_yuzdesi = float(input("Günlük artış yüzdesini giriniz (%): "))
maksimum_harcama = float(input("Maksimum harcayabileceğiniz miktarı giriniz (TL):"))

# Gün sayısı ve mevcut fiyatı hesaplamak için değişkenleri başlatın
gun = 0
mevcut_fiyat = ilk_gun_fiyati

# Müşterinin maksimum harcama miktarını aşana kadar döngüyü sürdürün
while mevcut_fiyat <= maksimum_harcama:
    print(f"{gun+1}. gün fiyatı: {mevcut_fiyat:.2f}")
    gun += 1
    mevcut_fiyat += mevcut_fiyat * (artis_yuzdesi / 100)

# Müşterinin ürünü satın alabileceği gün sayısını yazdırın
print(f"Müşteri ürünü {gun} gün içinde satın alabilir.")