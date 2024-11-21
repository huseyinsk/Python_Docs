ay = input("Bir ay giriniz.")
if ay in ("ocak", "Ocak", "OCAK") :
    print(f"{ay} 31 gündür.")
elif ay in ("şubat", "Şubat", "ŞUBAT") :
    print(f"{ay} 28 gündür.")
elif ay in ("mart", "Mart", "MART") :
    print(f"{ay} 31 gündür.")
elif ay in ("nisan", "Nisan", "NİSAN") :
    print(f"{ay} 30 gündür.")
elif ay in ("mayıs", "Mayıs", "MAYIS") :
    print(f"{ay} 31 gündür.")
elif ay in ("haziran", "Haziran", "HAZİRAN") :
    print(f"{ay} 30 gündür.")
elif ay in ("temmuz", "Temmuz", "TEMMUZ") :
    print(f"{ay} 31 gündür.")
elif ay in ("ağustos", "Ağustos", "AĞUSTOS") :
    print(f"{ay} 31 gündür.")
elif ay in ("eylül", "Eylül", "EYLÜL") :
    print(f"{ay} 30 gündür.")
elif ay in ("ekim", "Ekim", "EKİM") :
    print(f"{ay} 31 gündür.")
elif ay in ("kasım", "Kasım", "KASIM") :
    print(f"{ay} 30 gündür.")
elif ay in ("aralık", "Aralık", "ARALIK") :
    print(f"{ay} 31 gündür.")
else:
    print("Lütfen bir ay giriniz.")
