#Bu program, kullanıcıya bir parola soruyor.
#Eğer kullanıcının girdiği parola içinde Türkçe 
#karakterlerden herhangi biri varsa kullanıcıyı 
#Türkçe karakter kullanmaması konusunda uyarıyor.

tr_harfler = "şçöğüİı"

parola = input("Parolanız: ")

for karakter in parola:
    if karakter in tr_harfler:
        print("parolada Türkçe karakter kullanılamaz")
