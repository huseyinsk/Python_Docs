# Terim sayısını al
nterms = int(input("Terim sayısı kaçtır? "))

# İlk iki terim
n1, n2 = 0, 1
count = 0

# Terim sayısının geçerli olup olmadığını kontrol et
if nterms <= 0:
    print("Lütfen pozitif bir tamsayı giriniz")
# Eğer yalnızca bir terim varsa, n1'i döndür
elif nterms == 1:
    print(f"Fibonacci dizisi {nterms} terim için:")
    print(n1)
# Fibonacci dizisini oluştur
else:
    print("Fibonacci dizisi:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        # Değerleri güncelle
        n1 = n2
        n2 = nth
        count += 1
