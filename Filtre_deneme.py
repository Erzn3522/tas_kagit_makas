import cv2
import numpy as np


Kamera = cv2.VideoCapture(0)
while True:
    ret, Kare = Kamera.read()
    Kesilmiş_Kare = Kare[0:250, 0:250]

    Kesilmiş_Kare_HSV = cv2.cvtColor(Kesilmiş_Kare, cv2.COLOR_BGR2HSV)

    Alt_Degerler = np.array([0, 50, 90])
    Ust_Degerler = np.array([70, 225, 225])

    Renk_Filtresi_Sonucu = cv2.inRange(Kesilmiş_Kare_HSV, Alt_Degerler, Ust_Degerler)


    kernel = np.ones((15,15),np.float32)/225
    smoothed = cv2.filter2D(Renk_Filtresi_Sonucu,-1,kernel)
    blur=cv2.GaussianBlur(Renk_Filtresi_Sonucu,(15,15),0)
    median=cv2.medianBlur(Renk_Filtresi_Sonucu,15)
    bileteral=cv2.bilateralFilter(Renk_Filtresi_Sonucu,15,150,150)
    kenarlar=cv2.Canny(Renk_Filtresi_Sonucu,100,100)

    cv2.imshow("Kesilmiş_Kare", Kesilmiş_Kare)
    cv2.imshow("Kare", Kare)
    cv2.imshow("Renk_Filtresi_Sonucu", Renk_Filtresi_Sonucu)

    cv2.imshow("blur", blur)
    cv2.imshow("smoothed", smoothed)
    cv2.imshow("median", median)
    cv2.imshow("bilateral",bileteral)
    cv2.imshow("kenarlar", kenarlar)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
Kamera.release()
cv2.destroyAllWindows()