yaş = int(input("Yaşınız: "))

if yaş == 18:
    print("18 iyidir!")

elif yaş < 0:
    print("Yok canım, daha neler!...")

elif yaş < 18:
    print("Genç bir kardeşimizsin!")

elif yaş > 18:
    print("Eh, artık yaş yavaş yavaş kemale eriyor!")