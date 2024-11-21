#ALIŞTIRMA 6:
#Rastgele bir parola oluşturan bir fonksiyon yazınız.Parola 7 ile 10 karakter arasında rastgele uzunlukta
#olmalıdır.Her karakter, ASCII tablosunda 33 ila 126. konumlardan rastgele seçilmelidir.Fonksiyonunuz
#herhangi bir parametre almayacaktır. Tek sonucu olarak rastgele oluşturulan parolayı döndürecektir.

import random

def making_random_password():
    """
    Ascii tablosunun 33 ile 126 konumlarından rastgele seçilerek
    bir parola oluşturur.
    """
    x = random.randint(7,10)
    for i in range(1,x+1):
        y = random.randint(33,126)
        chr(y)
        print(chr(y), end="")

making_random_password()

#ALIŞTIRMA 6:
#Rastgele bir parola oluşturan bir fonksiyon yazınız.Parola 7 ile 10 karakter arasında rastgele uzunlukta
#olmalıdır.Her karakter, ASCII tablosunda 33 ila 126. konumlardan rastgele seçilmelidir.Fonksiyonunuz
#herhangi bir parametre almayacaktır. Tek sonucu olarak rastgele oluşturulan parolayı döndürecektir.
