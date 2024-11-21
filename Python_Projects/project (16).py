#Palindrom, hem baştan hem de sondan aynı şekilde okunduğunda aynı kalan kelime veya ifadelerdir.
#Örneğin "anna", "level", "rotor", "talat" veya "madam" gibi kelimeler palindromlara örnektir.
#Sizden istenen, kullanıcının gireceği herhangi bir kelimenin (büyük veya küçük harf fark etmeksizin)
#palindrom olup olmadığını kontrol edecek ve sonucu ekrana yazacak bir Python programı yazmanızdır.

#Fesih/Ozan Hoca bir kelimenin tersi nasıl alınır gösterdi mi hatırlamıyorum ancak substringi öğretti.
#işimi garantiye almak amaçlı iki şekilde yazdım kodu

x = input("Kontrol etmek istediğiniz kelimeyi giriniz: ").lower()
y = x[::-1]

if x == y:
    print(f'Girmiş olduğunuz "{x}" kelimesi, bir polindrom kelimedir.')
else:
    print(f'Girmiş olduğunuz "{x}" kelimesi, bir polindrom kelime değildir.')


#Palindrom, hem baştan hem de sondan aynı şekilde okunduğunda aynı kalan kelime veya ifadelerdir.
#Örneğin "anna", "level", "rotor", "talat" veya "madam" gibi kelimeler palindromlara örnektir.
#Sizden istenen, kullanıcının gireceği herhangi bir kelimenin (büyük veya küçük harf fark etmeksizin)
#palindrom olup olmadığını kontrol edecek ve sonucu ekrana yazacak bir Python programı yazmanızdır.

