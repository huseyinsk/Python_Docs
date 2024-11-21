# 2. dereceden denklemi çözecek python programı:
# delta = b**2 - 4*a*c ve x = (-b -/+ (kök delta)) / (2*a)
# a*x**2 + b*x + c = 0 denklemi

a = int(input("a değerini giriniz: "))
b = int(input("b değerini giriniz: "))
c = int(input("c değerini giriniz: "))
delta = (b**2) - (4*a*c)
first_x = ((-b)-(delta**2))/(2*a)
second_x = ((-b)+(delta**2))/(2*a)

if delta == 0:
    print(f"Tek bir kök vardır, bulunan kök: {first_x}")
elif delta < 0:
    print(f"İki adet sanal kök vardır, bulunan kökler: {first_x},{second_x}")
elif delta > 0:
    print(f"İki adet reel kökü vardır, bulunan kökler: {first_x},{second_x}")
