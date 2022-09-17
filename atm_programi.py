import datetime
bakiye = 1000
hesaphareketleri = []

while True:
            
    print("-----------------------------------\n\nATM Programına Hoş Geldiniz ;)\n\nYapmak İstediğiniz İşlemi Seçiniz ;\n\n1) Bakiye Sorgulama\n\n2) Para Yatırma \n\n3) Para Çekme\n\n4) Hesap Hareketleri \n\n5) Çıkış için \n\n-----------------------------------")

    kyi = input("Yapmak istediğiniz işlem nedir ? : ")

    if (kyi == "1"):
        print("Bakiyeniz : ", bakiye, "₺'dir")
        an = datetime.datetime.now()
        hesaphareketleri.append(f"{str(an)}  Bakiye Sorgulama İşlemi Yapıldı : {str(bakiye)}" + "₺'dir")



    if (kyi == "2"):
        kyt = int(input("Yatırmak İstediğiniz Tutar : "))
        bakiye = bakiye + kyt
        print("Yatırdığınız Tutar : ", kyt, "\nŞu an ki Bakiyeniz ise : ", bakiye)
        an = datetime.datetime.now()
        hesaphareketleri.append(f"{str(an)}  Para Yatırma İşlemi Yapıldı : {kyt}₺  Güncel Tutar : {str(bakiye)}" + "₺'dir")



    if (kyi == "3"):
        kçt = int(input("Çekmek İstediğiniz Tutar : "))
        if (bakiye < kçt ):
            print("Yetersiz Bakiye !")
        else:
            bakiye = bakiye - kçt
            print("Çektiğiniz Tutar : ", kçt, "\nŞu an ki Bakiyeniz ise : ", bakiye)
            an = datetime.datetime.now()
            hesaphareketleri.append(f"{str(an)}  Para Çekleme İşlemi Yapıldı : {kçt}₺  Güncel Tutar : {str(bakiye)}" + "₺'dir")



    if(kyi == "4"):
        metin=""
        for kelime in hesaphareketleri:
            metin=metin+kelime+"\n"
        print(metin)

    if(kyi == "5"):
        break

            

        
