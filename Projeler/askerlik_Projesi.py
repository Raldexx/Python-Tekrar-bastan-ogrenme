yas = int(input("Yasinizi Giriniz: "))
okul = (input("Okula gidiyormusun? evet: y, Hayir:n "))

if yas >= 18 and okul == "h":
    print("Askere Gelme Yasiniz Geldi!")

elif yas >= 18 and okul == "y":
    print("Okulunuz Bittiginde Askere Geleceksiniz!")

else:
    print("Askerlik yasiniz gelmedi!")

