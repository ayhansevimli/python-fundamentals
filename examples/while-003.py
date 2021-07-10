#Aksi belirtilmediği sürece kullanıcıya
#aşağıdaki soruyu sormaya devam et!
while True:
    soru = input("Nasılsınız, iyi misiniz?")

    #Eğer kullanıcı 'q' tuşuna basarsa...
    if soru == "q":
        break #döngüyü kır ve programdan çık.