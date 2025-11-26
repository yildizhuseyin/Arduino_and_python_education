# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 22:56:12 2025

@author: HY
"""

import cv2 # Görüntü işleme kütüphanesi 
import numpy as np
import time as t
import matplotlib.pyplot as plt #Çizim kütüphanesini çağır

import pyfirmata # firmata kütüphanesini yüklüyoruz

port='COM3'
board = pyfirmata.Arduino(port) # 'COM3 seri portunda yer alan arduino ya bağlan 
print(port,'Arduino bağlantısı kuruldu ..') # Ekrana bağlandığını yaz. 

led_mavi = board.get_pin('d:11:p')
led_yesil = board.get_pin('d:6:p')
led_kirmizi = board.get_pin('d:10:p')
led_buzzer = board.get_pin('d:5:o')

led_mavi.write(1); t.sleep(0.2)
led_yesil.write(1); t.sleep(0.2)
led_kirmizi.write(1)

t.sleep(1)
led_mavi.write(0)
led_yesil.write(0)
led_kirmizi.write(0)



# Kamera görüntüsü oku ve led yak 
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
    Lower=(0,0,170)
    Upper=(150,150,250)
    mask=cv2.inRange(blured_resim,Lower,Upper)# self.LowerRed,self.UpperRed
    ort_mask=np.mean(mask)
    print(success,round(sure,2),round(ort_b,2),round(ort_g,2),round(ort_r,2),ort_mask)
    led_mavi.write(abs(ort_b-100)/255)
    led_yesil.write(abs(ort_g-100)/255)
    led_kirmizi.write(abs(ort_r-100)/255)

    if ort_mask>20:
        led_buzzer.write(1.0)
        print('kırmızı nesne')
    else: 
        led_buzzer.write(0)
    if success:
        cv2.imshow('Resim', yeni_resim)
        cv2.imshow('Blured', blured_resim)
        cv2.imshow('S & B Resim', S_B_resim)
        cv2.imshow('Maske', mask)
        print('Resim başarı ile okundu')
    
    if cv2.waitKey(33) == 27: # Escape tuşuna basılırsa durdur 
        print('Durduruldu')
        break
    t.sleep(dt)
cap.release()

board.exit() # Port bağlantısını kes 

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