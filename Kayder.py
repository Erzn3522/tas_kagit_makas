import cv2
import numpy as np
import os

Kamera = cv2.VideoCapture(0)
kernel = np.ones((15,15),np.uint8)
isim= "Makas"
while True:
    ret, Kare = Kamera.read()
    Kesilmiş_Kare = Kare[0:250,0:250]
    Kesilmiş_Kare_HSV = cv2.cvtColor(Kesilmiş_Kare,cv2.COLOR_BGR2HSV)



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
        cv2.imshow("El_Resim", El_Resim)




    cv2.imshow("Kesilmiş_Kare", Kesilmiş_Kare)
    cv2.imshow("Kare", Kare)
    cv2.imshow("Renk_Filtresi_Sonucu", Renk_Filtresi_Sonucu)
    cv2.imshow("Sonuc",Sonuc)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.imwrite("Veri/"+isim+".jpg",El_Resim)
Kamera.release()
cv2.destroyAllWindows()