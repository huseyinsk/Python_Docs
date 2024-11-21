#ALIŞTIRMA 5:
#Çoğu kişi, özellikle akıllı telefonlar gibi küçük cihazlarda yazı yazarken büyük harfleri doğru kullanmaz.
#Bu soruda, bir stringdeki uygun karakterleri büyük harfle yazan donuştur adına bir fonksiyon yazınız.
#Stringdeki ilk karakter büyük harfle yazılmalıdır.Küçük "i" harfi, önünde de boşluk varsa,
#büyük «I» harfi ile değiştirilmelidir. İpucu: Bir string methodu olan replace inceleyiniz.

the_message = input("Yazınızı giriniz: ")

def edit_text_function():
    """
    İlk karakteri büyük harfe dönüştürür ve
    küçük i harfini I yapar.
    """
    changed_the_message = the_message.capitalize()
    changed_the_message_1 = changed_the_message.replace(" i", " I")
    print(changed_the_message_1)

edit_text_function()


#ALIŞTIRMA 5:
#Çoğu kişi, özellikle akıllı telefonlar gibi küçük cihazlarda yazı yazarken büyük harfleri doğru kullanmaz.
#Bu soruda, bir stringdeki uygun karakterleri büyük harfle yazan donuştur adına bir fonksiyon yazınız.
#Stringdeki ilk karakter büyük harfle yazılmalıdır.Küçük "i" harfi, önünde de boşluk varsa,
#büyük «I» harfi ile değiştirilmelidir. İpucu: Bir string methodu olan replace inceleyiniz.
