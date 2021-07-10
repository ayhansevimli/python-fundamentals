giris = """
(1) topla
(2) cikar
(3) carp
(4) bol
(5) karesini hesapla
(6) karekok hesapla
"""
print(giris)

soru = input ("Yapmak istediginiz islemin numarasini girin : ")

if soru == "1":
    sayi1 = int(input("Toplama islemi icin ilk sayiyi girin = "))
    sayi2 = int(input("Toplama islemi icin ikinci sayiyi girin = "))
    print(sayi1, "+", sayi2, "=", sayi1 + sayi2)
elif soru == "2":
    sayi1 = int(input("Cikarma islemi icin ilk sayiyi girin = "))
    sayi2 = int(input("Cikarma islemi icin ikinci sayiyi girin = "))
    print(sayi1, "-", sayi2, "=", sayi1 - sayi2)
elif soru == "3":
    sayi1 = int(input("Carpma islemi icin ilk sayiyi girin = "))
    sayi2 = int(input("Carpma islemi icin ikinci sayiyi girin = "))
    print(sayi1, "*", sayi2, "=", sayi1 * sayi2)
elif soru == "4":
    sayi1 = int(input("Bolme islemi icin ilk sayiyi girin = "))
    sayi2 = int(input("Bolme islemi icin ikinci sayiyi girin = "))
    print(sayi1, "/", sayi2, "=", sayi1 / sayi2)
elif soru == "5":
    sayi1 = int(input("Kare hesaplama islemi icin sayiyi girin = "))
    print(sayi1, " in karesi = ", sayi1**2)
elif soru == "6":
    sayi1 = int(input("Karekok islemi icin ilk sayiyi girin = "))
    print(sayi1, " 'in karekoku = ", sayi1 **0.5)
else:
    print("Yanlis secenek girildi...")
    print("Asagidaki seceneklerden birini giriniz : ", giris)

    
    