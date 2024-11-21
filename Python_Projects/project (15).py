#Palindrom, hem baştan hem de sondan aynı şekilde okunduğunda aynı kalan kelime veya ifadelerdir.
#Örneğin "anna", "level", "rotor", "talat" veya "madam" gibi kelimeler palindromlara örnektir.
#Sizden istenen, kullanıcının gireceği herhangi bir kelimenin (büyük veya küçük harf fark etmeksizin)
#palindrom olup olmadığını kontrol edecek ve sonucu ekrana yazacak bir Python programı yazmanızdır.


x = input("Kontrol etmek istediğiniz kelimeyi giriniz: ").lower()
y = ""

for z in range(len(x)-1,-1,-1):
    y += x[z]

if x[:] == y[:] :
    print(f'Girmiş olduğunuz "{x}" kelimesi bir palindrom kelimedir.')
else:
    print(f'Girmiş olduğunuz "{x}" kelimesi bir palindrom kelime değildir.')


#Palindrom, hem baştan hem de sondan aynı şekilde okunduğunda aynı kalan kelime veya ifadelerdir.
#Örneğin "anna", "level", "rotor", "talat" veya "madam" gibi kelimeler palindromlara örnektir.
#Sizden istenen, kullanıcının gireceği herhangi bir kelimenin (büyük veya küçük harf fark etmeksizin)
#palindrom olup olmadığını kontrol edecek ve sonucu ekrana yazacak bir Python programı yazmanızdır.
