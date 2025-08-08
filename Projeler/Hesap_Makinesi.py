# Ilk sayiyi aliyoruz
sayi1 = float(input("Ilk sayiyi girin: "))

# Ikinci sayiyi aliyoruz
sayi2 = float(input("Ikinci sayiyi girin: "))

# Yapmak istedigi islemi aliyoruz
islem = input("Yapmak istediginiz islemi girin (+, -, *, /): ")

# Islemi kontrol edip sonucu hesapliyoruz
if islem == '+':
    sonuc = sayi1 + sayi2
elif islem == '-':
    sonuc = sayi1 - sayi2
elif islem == '*':
    sonuc = sayi1 * sayi2
elif islem == '/':
    # Sifira bolme hatasini kontrol ediyoruz
    if sayi2 == 0:
        print("Hata: Bir sayiyi sifira bolemezsiniz.")
    else:
        sonuc = sayi1 / sayi2
else:
    print("Gecersiz islem girdiniz.")
    
# Eger bir sonuc hesaplanmissa ekrana yazdiriyoruz
if 'sonuc' in locals():
    print("Sonuc:", sonuc)