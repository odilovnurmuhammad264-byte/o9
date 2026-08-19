parol = "2222"
balans = 100000

while True:
    kirilgan = input("Parolni kiriting: ")
    if kirilgan == parol:
        print("\nKirish mufaqiylatli\n")
        break

while True:
    print("1 Balansni korish")
    print("2 Pul qoshish")
    print("3 Pul yechish")
    print("4 Chiqish")

    tanlov = input("Tanlang: ")

    if tanlov == "1":
        print(f"Balans: {balans} som\n")

    elif tanlov == "2":
        miqdor = int(input("Pul miqdori: "))
        balans += miqdor
        print("Pul qoshildi\n")

    elif tanlov == "3":
        miqdor = int(input("Pul miqdori: "))
        if miqdor <= balans:
            balans -= miqdor
            print("Pul yechildi\n")
        else:
            print("Hisobda mablag yetarli emas\n")

    elif tanlov == "4":
        print("Dastur tugadi")
        break

    else:
        print("Notogri tanlov\n")