x = int(input("Notunuz: "))

if x > 100 or x < 0:
    print("Böyle bir not yok")

#90 sayısı x'ten küçük veya x'e eşit,
#x sayısı 100'den küçük veya 100'e eşit ise,
#Yani x, 90 ile 100 arasında bir sayı ise
elif 90 <= x <= 100:
    print("A aldınız.")

#80 sayısı x'ten küçük veya x'e eşit,
#x sayısı 89'dan küçük veya 89'a eşit ise,
#Yani x, 80 ile 89 arasında bir sayı ise
elif 80 <= x <= 89:
    print("B aldınız.")

elif 70 <= x <= 79:
    print("C aldınız.")

elif 60 <= x <= 69:
    print("D aldınız.")

elif 0 <= x <= 59:
    print("F aldınız.")