ehliyet = False
araba = True

if ehliyet and araba:
    print("Sahip oldugun arabayi rahatca kullanabilirsin") 

elif araba and not ehliyet:
    print("Ehliyetin yok ama araban var")

elif ehliyet or araba:
    print("Araba kullanmana cok az kaldi")

else: 
    print("Araba kullanamazsin")

#and operatörü: ikiside varsa isleme girer.
#or operatörü: ikisinden birisi varsa isleme girer.
#not operatörü: değil anlamına gelir.








