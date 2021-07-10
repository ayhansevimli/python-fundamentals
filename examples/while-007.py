#kullanıcıya bir parola belirletirken, 
#belirlenecek parolanın 8 karakterden uzun, 
#3 karakterden kısa olmamasını sağlamak

while True:
    parola = input("Bir parola belirleyin : ")

    if not parola:
        print("Parola bolumu bos gecilemez!!!")
    elif len(parola) > 8 or len (parola) < 3 :
        print("Parola 8 karekterden uzun veya 3 karekterden kisa olmamali")
    else:
        print("Yeni parolaniz = ", parola)
        break

