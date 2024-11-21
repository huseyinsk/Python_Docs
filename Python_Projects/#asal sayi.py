# ASAL SAYI

x = int(input("Bir Sayı giriniz: "))
if x > 1:
    """
    asal yapan kod
    """
    for i in range(2, x):
        if x % i == 0:
            print("Asal sayı değildir.")
            break
    else:
        print("bir asal sayıdır.")
    """
    asal yapan kod
    """
elif x == 1:
    print("Bir asal sayı değildir.")
else:
    print("asf")
