# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 22:56:12 2025

@author: HY
"""

import cv2 # Görüntü işleme kütüphanesi 
import numpy as np
import time as t
import matplotlib.pyplot as plt #Çizim kütüphanesini çağır


# ilk görüntüyü okuma 
cv2.namedWindow("preview")
cap=cv2.VideoCapture(0) # 0 numaralı kamerayı aç 

if cap.isOpened(): # try to get the first frame
    success, first_frame = cap.read()
    cv2.imshow('İlk Resim', first_frame)
else:
    success = False

cv2.destroyAllWindows()
cap.release()






# Kamera görüntüsü izleme 
cap=cv2.VideoCapture(0) # 0 numaralı kamerayı aç 
if cap.isOpened(): # İlk görseli oku 
    success, first_frame = cap.read()
else:
    success = False
    
sure=0; dt=0.1
while success: # Eğer kamera açılmışsa Sonsuz bir döngü oluştur 
    sure+=dt # zamanı ilerlet 
    success, frame = cap.read() # görüntü oku 
    print(success,round(sure,2)) # Bİlgileri ekrana yaz 
    if success:
        cv2.imshow('Resim', frame) # Resim okundu ise ekranda göster 
        print('Resim başarı ile okundu')
    
    if cv2.waitKey(33) == 27: # Escape tuşuna basılırsa durdur 
        print('Durduruldu')
        break
    t.sleep(dt)
cap.release()







# Kamera görüntüsü oku ve renk filtresi oluştur  

cap=cv2.VideoCapture(0) # 0 numaralı kamerayı aç 
if cap.isOpened(): # ilk görüntüyü oku 
    success, first_frame = cap.read()
else:
    success = False
sure=0; dt=0.1

while success: # Sonsuz bir döngü oluştur 
    sure+=dt
    success, frame = cap.read()
    yeni_resim=cv2.resize(frame,[300,240], interpolation = cv2.INTER_AREA) # Resmin boyutunu küçült 
    blured_resim = cv2.GaussianBlur(yeni_resim, (3,3),20) # Bulanıklaştır 
    # S_B_resim=blured_resim[:,:,0] # Mavi / Blue kanal
    # S_B_resim=blured_resim[:,:,1] # Yeşil Green kanal
    S_B_resim=blured_resim[:,:,2] # Kırmızı / red kanal 
    ort_b=np.mean(blured_resim[:,:,0])
    ort_g=np.mean(blured_resim[:,:,1])
    ort_r=np.mean(blured_resim[:,:,2])
    print(success,round(sure,2),round(ort_b,2),round(ort_g,2),round(ort_r,2))
    if success:
        cv2.imshow('Resim', yeni_resim)
        cv2.imshow('Blured', blured_resim)
        cv2.imshow('S & B Resim', S_B_resim)
        print('Resim başarı ile okundu')
    
    if cv2.waitKey(33) == 27: # Escape tuşuna basılırsa durdur 
        print('Durduruldu')
        break
    t.sleep(dt)
cap.release()



"""
say=0
while True:
    say+=1
    try:
        print(say)
        t.sleep(0.1)
    except:
        print("İşlem esnasında hata oluştu")
        break
        
        
    if keyboard.is_pressed('esc'):
        break
"""