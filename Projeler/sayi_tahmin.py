import random

cevap = random.randint(1, 100)

while True:
    tahmin_str = input("\nSayı tahmin oyununa başlamak için 1 ile 100 arasında bir sayı tahmin et: ")

    if not tahmin_str.isdigit():
        print("Lütfen geçerli bir sayı girin.")
        continue

    tahmin = int(tahmin_str)

    if tahmin == cevap:
        print("\nTebrikler, oyunu kazandın!")
        break
    elif tahmin < cevap:
        print("\nDaha büyük bir sayı gir.")
    else:  # tahmin > cevap
        print("\nDaha küçük bir sayı gir.")