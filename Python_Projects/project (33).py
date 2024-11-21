#ALIŞTIRMA 3:
#Taksi ücretleri 8TL biniş ücreti artı her 140 metrede 0.35 TL ücretten oluşur.Tek parametresi olarak gidilen
#mesafeyi (kilometre cinsinden) alan ve sonuç olarak toplam ücretini veren bir fonksiyon yazınız.

distance_km = float(input("Gidilen mesafeyi (kilometre cinsinden) giriniz: "))
starting_payment = 8 

def total_payment_function(distance_km):
    """
    Taksi ücretini hesaplayan fonksiyon
    """
    
    x = (distance_km*1000) // 140
    total_payment = (x * 0.35) + starting_payment 
    print("Toplam taksi ücreti: ", total_payment)

total_payment_function(distance_km)

#ALIŞTIRMA 3:
#Taksi ücretleri 8TL biniş ücreti artı her 140 metrede 0.35 TL ücretten oluşur.Tek parametresi olarak gidilen
#mesafeyi (kilometre cinsinden) alan ve sonuç olarak toplam ücretini veren bir fonksiyon yazınız.
