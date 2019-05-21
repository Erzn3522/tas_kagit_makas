import cv2
import numpy as np
import os
import random



Kamera = cv2.VideoCapture(0)
kernel = np.ones((15,15),np.uint8)

def ResimFarkBul (Resim1,Resim2):
    Resim2=cv2.resize(Resim2,(Resim1.shape[1],Resim1.shape[0]))
    Fark_Resim =cv2.absdiff(Resim1,Resim2)
    Fark_Sayi = cv2.countNonZero(Fark_Resim)
    return Fark_Sayi

def VeriYukle():
    Veri_isimler = []
    Veri_Resimler = []

    Dosyalar = os.listdir("Veri/")
    for Dosya in Dosyalar:
        Veri_isimler.append(Dosya.replace(".jpg",""))
        Veri_Resimler.append(cv2.imread("Veri/"+Dosya,0))
    return Veri_isimler,Veri_Resimler

def Sınıflandır (El_Resim,Veri_isimler,Veri_Resimler):
    Min_Index = 0
    Min_Deger = ResimFarkBul(El_Resim,Veri_Resimler[0])

    for t in range(len(Veri_isimler)):
        Fark_Deger = ResimFarkBul(El_Resim,Veri_Resimler[t])
        if(Fark_Deger<Min_Deger):
            Min_Deger = Fark_Deger
            Min_Index=t
    return  Veri_isimler[Min_Index]


Veri_isimler, Veri_Resimler = VeriYukle()

while True:
    ret, Kare = Kamera.read()
    Kesilmiş_Kare = Kare[0:250,0:250]
    Kesilmiş_Kare_HSV = cv2.cvtColor(Kesilmiş_Kare,cv2.COLOR_BGR2HSV)
    c=0


    Alt_Degerler = np.array([0,50,90])
    Ust_Degerler= np.array([70,225,225])

    Renk_Filtresi_Sonucu = cv2.inRange(Kesilmiş_Kare_HSV,Alt_Degerler,Ust_Degerler)
    Sonuc = Kesilmiş_Kare.copy()
    _, cnts,_ = cv2.findContours(Renk_Filtresi_Sonucu,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    Max_Genislik = 0
    Max_Uzunluk = 0
    Max_Index = -1

    for t in range (len(cnts)):
        cnt = cnts[t]
        x,y,w,h = cv2.boundingRect(cnt)
        if (w > Max_Genislik and h > Max_Uzunluk):
            Max_Uzunluk = h
            Max_Genislik = w
            Max_Index = t

    if(len(cnts)>0):
        x,y,w,h = cv2.boundingRect(cnts[Max_Index])
        cv2.rectangle(Sonuc,(x,y),(x+w,y+h),(0,255,0),2)
        El_Resim = Renk_Filtresi_Sonucu[y:y+h,x:x+w]
        cv2.imshow("El_Resim",El_Resim)

        print(Sınıflandır(El_Resim,Veri_isimler,Veri_Resimler))

        taskagitmakas = ["Tas", "Kagit", "Makass"]
        a= ""
        Tas = taskagitmakas[0]
        Kagit = taskagitmakas[1]
        Makass = taskagitmakas[2]
        gir = Sınıflandır(El_Resim,Veri_isimler,Veri_Resimler)


    if (len(gir) == len(a)):
        print("şuan el görüntüsü yok")
        gir = Sınıflandır(El_Resim, Veri_isimler, Veri_Resimler)



    elif(len(gir) != len(a)):

        a = random.choice(taskagitmakas)

        print("BİLGİSAYAR", a, "SEÇTİ")
        print(len(gir))
        print("a:", len(a))


        if gir == Kagit:
            if Kagit == a:
                print("BERABERE")
                print("----------")


            elif Tas == a:
                print("KAZANDINIZ")
                print("----------")



            elif Makass == a:
                print("KAYBETTİNİZ")
                print("----------")


        elif gir == Tas:
            if Tas == a:
                print("BERABERE")
                print("----------")

            elif Kagit == a:
                print("KAYBETTİNİZ")
                print("----------")

            elif Makass == a:
                print("KAZANDINIZ")
                print("----------")

        elif gir == Makass:
            if Makass == a:
                print("BERABERE")
                print("----------")


            elif Tas == a:
                print("KAYBETTİNİZ")
                print("----------")

            elif Kagit == a:
                print("KAZANDINIZ")
                print("----------")
                

    cv2.imshow("Kare", Kare)
    cv2.imshow("Kesilmiş_Kare", Kesilmiş_Kare)
    cv2.imshow("Renk_Filtresi_Sonucu", Renk_Filtresi_Sonucu)
    cv2.imshow("Sonuc",Sonuc)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
Kamera.release()
cv2.destroyAllWindows()
