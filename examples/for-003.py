#sayılar değişkeni içinde i adını verdiğimiz her bir öğe için:
#eğer sayıya dönüştürülmüş i değeri 3‘ten büyükse:
#i öğesini ekrana basma işlemi gerçekleştir!

sayılar = "123456789"

for i in sayılar:
    if int(i) > 3:
        print(i)
        