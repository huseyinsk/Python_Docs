#Bir parolanın güçlü olup olmadığını belirleyen bir fonksiyon yazınız. Güçlü parola; en az 8 karakter uzunluğunda,
#en az bir büyük ve bir küçük harf ve, en az bir rakam içeren bir paroladır. Fonksiyon,tek parametre olarak kendisine
#iletilen parolayı alır ve güçlü bir arola ise «Güçlü parola» değilse «Zayıf parola» ifadelerini ekrana yazar.

password = input("Test etmek istediğiniz parolayı giriniz: ")
upper_letters = ["A", "B", "C", "Ç", "D", "E", "F", "G", "Ğ", "H", "I", "İ", "J", "K", "L", "M", "N", "O", "Ö", "P", "R", "S", "Ş", "T", "U", "Ü", "V", "Y", "Z"]
lower_letters = ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k", "l", "m", "n", "o", "ö", "p", "r", "s", "ş", "t", "u", "ü", "v", "y", "z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
list_password = list(password)

def checking_password_function(password):
    """
    Bir parolanın güçlü olup olmadıgını kontrol eden
    fonksiyondur.
    """

    if len(password) <= 7:
        print(f"Girmiş olduğunuz {password} parolanız bir zayıf paroladır.")

    else:
        has_lower = any(char in lower_letters for char in password) #Fesih hoca derste any'i anlatmadım ama kullanabilirsiniz dedi.
        has_upper = any(char in upper_letters for char in password)  
        has_number = any(char in numbers for char in password)  

        if not (has_lower and has_upper and has_number) :
            print(f"Girmiş olduğunuz {password} parolanız bir zayıf paroladır.")
        else:
            print(f"Girmiş olduğunuz {password} parolanız bir güçlü paroladır.")
            
checking_password_function(password)

#Bir parolanın güçlü olup olmadığını belirleyen bir fonksiyon yazınız. Güçlü parola; en az 8 karakter uzunluğunda,
#en az bir büyük ve bir küçük harf ve, en az bir rakam içeren bir paroladır. Fonksiyon,tek parametre olarak kendisine
#iletilen parolayı alır ve güçlü bir arola ise «Güçlü parola» değilse «Zayıf parola» ifadelerini ekrana yazar.

