tekrar = 1

while tekrar <= 3:
    print("tekrar: ", tekrar)
    tekrar += 1
    input("Nasılsınız, iyi misiniz?")
    print("bool değeri: ", bool(tekrar <= 3))