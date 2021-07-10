giris = """
(1) topla
(2) cikar
(3) carp
(4) bol
(5) karesini hesapla
(6) karekok hesapla
"""

print (giris)

anahtar = 1

while True:
    soru = input("Yapmak istediginiz islemin numarasini girin (Cikmak icin q) : ")
    if soru == "q":
        print("Programdan cikiliyor ...")
        break
    elif soru == "1":
        sayi1= int(input("Toplama icin sayi1 girin : "))
        sayi2= int(input("Toplama icin sayi2 girin : "))
        print(sayi1, " + ", sayi2," = " , sayi1 + sayi2)
        print("Asagidaki seceneklerden birini giriniz : ", giris)
    elif soru == "2":
        sayi1= int(input("Cikarma icin sayi1 girin : "))
        sayi2= int(input("Cikarma icin sayi2 girin : "))
        print(sayi1, " - ", sayi2," = " , sayi1-sayi2)
        print("Asagidaki seceneklerden birini giriniz : ", giris)
    elif soru == "3":
        sayi1= int(input("Carpma icin sayi1 girin : "))
        sayi2= int(input("Carpma icin sayi2 girin : "))
        print(sayi1, " * ", sayi2," = " ,sayi1*sayi2)
        print("Asagidaki seceneklerden birini giriniz : ", giris)
    elif soru == "4":
        sayi1= int(input("Bolme icin sayi1 girin : "))
        sayi2= int(input("Bolme icin sayi2 girin : "))
        print(sayi1, " / ", sayi2," = " , sayi1/sayi2)
        print("Asagidaki seceneklerden birini giriniz : ", giris)
    elif soru == "5":
        sayi1= int(input("Kare hesaplama icin sayi1 girin : "))
        print(sayi1, "'in karesi = " , sayi1**2)
        print("Asagidaki seceneklerden birini giriniz : ", giris)
    elif soru == "6":
        sayi1= int(input("Karekok hesaplama icin sayi1 girin : "))
        print(sayi1, "'in karekoku = " , sayi1**0.5)
        print("Asagidaki seceneklerden birini giriniz : ", giris)

    else:
        print("Yanlis secenek girildi.")
        print("Asagidaki seceneklerden birini giriniz : ", giris)



    
        