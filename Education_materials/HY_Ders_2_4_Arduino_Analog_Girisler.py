# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 21:42:45 2025

@author: HY
"""


import pyfirmata # firmata kütüphanesini yüklüyoruz
import time as t
import keyboard  # using module keyboard
# Pinleri değişken olarak atama 

# Analog sinyal okuma 
port='COM3'
board = pyfirmata.Arduino(port) # 'COM3 seri portunda yer alan arduino ya bağlan 
print(port,'Arduino bağlantısı kuruldu ..') # Ekrana bağlandığını yaz. 

analog_0 = board.get_pin('a:0:i') # 0 numaralı pini analog giriş olarak ayarla
analog_3 = board.get_pin('a:3:i') # 3 numaralı pini analog giriş olarak ayarla

iterator = pyfirmata.util.Iterator(board) # Sürekli olarak pin verilerini kontrol edecek bir iteratör tanımla 
iterator.start() # İteratörü çalıştır 
analog_0.enable_reporting() # 0 numaralı pinin okunma özelliğini aktif et. 
analog_3.enable_reporting() # 3 numaralı pinin okunma özelliğini aktif et. 

say=0
while True: # Sonsuz bir döngü oluştur 
    say+=1
    value_0=analog_0.read() # Pin değerini oku 
    value_3=analog_3.read() # Pin değerini oku 
    print(say,value_0,value_3) # sıra numarası ve pin değerini ekrana yaz. 
    if keyboard.is_pressed('esc'):
        break
    t.sleep(0.1)
board.exit() # Port bağlantısını kes 


# Analog sinyal okuma ve grafik çizme 
import pyfirmata # firmata kütüphanesini yüklüyoruz
import time as t
import keyboard  # using module keyboard

import matplotlib.pyplot as plt # Garfik kütüphanesini yükle 
import numpy as np

port='COM3'
board = pyfirmata.Arduino(port) # 'COM3 seri portunda yer alan arduino ya bağlan 
print(port,'Arduino bağlantısı kuruldu ..') # Ekrana bağlandığını yaz. 

analog_0 = board.get_pin('a:0:i') # 0 numaralı pini analog giriş olarak ayarla
analog_3 = board.get_pin('a:3:i') # 3 numaralı pini analog giriş olarak ayarla

iterator = pyfirmata.util.Iterator(board) # Sürekli olarak pin verilerini kontrol edecek bir iteratör tanımla 
iterator.start() # İteratörü çalıştır 
analog_0.enable_reporting() # 0 numaralı pinin okunma özelliğini aktif et. 
analog_3.enable_reporting() # 3 numaralı pinin okunma özelliğini aktif et. 

Data=[]
say=0
sure=0 
dt=0.1
while True: # Sonsuz bir döngü oluştur 
    say+=1
    sure=sure+dt
    value_0=analog_0.read() # Pin değerini oku 
    value_3=analog_3.read() # Pin değerini oku 
    print(say,value_0,value_3) # sıra numarası ve pin değerini ekrana yaz. 
    Data.append([sure,value_0,value_3])

    if keyboard.is_pressed('esc'):
        break
    t.sleep(dt)
board.exit() # Port bağlantısını kes 

# grafik olarak çiz 
fig = plt.figure()
ax = fig.add_subplot(111) #♦  projection='3d'
np_Data=np.array(Data)
ax.plot(np_Data[:,0],np_Data[:,1])
ax.plot(np_Data[:,0],np_Data[:,2])
ax.set_xlabel('t')
ax.set_ylabel('A')
ax.legend(['A0','A3'])




# Analog sinyal okuma, garafik çizme ve led kontrol 

import pyfirmata # firmata kütüphanesini yüklüyoruz
import time as t
import keyboard  # using module keyboard

import matplotlib.pyplot as plt # Garfik kütüphanesini yükle 
import numpy as np

port='COM3'
board = pyfirmata.Arduino(port) # 'COM3 seri portunda yer alan arduino ya bağlan 
print(port,'Arduino bağlantısı kuruldu ..') # Ekrana bağlandığını yaz. 

analog_0 = board.get_pin('a:0:i') # 0 numaralı pini analog giriş olarak ayarla
analog_3 = board.get_pin('a:3:i') # 3 numaralı pini analog giriş olarak ayarla

led_3=board.get_pin('d:3:p') # 3 numaralı pini dijital PWNM çıkış olarak ayarla
led_6=board.get_pin('d:6:p') # 6 numaralı pini dijital PWNM çıkış olarak ayarla

iterator = pyfirmata.util.Iterator(board) # Sürekli olarak pin verilerini kontrol edecek bir iteratör tanımla 
iterator.start() # İteratörü çalıştır 
analog_0.enable_reporting() # 0 numaralı pinin okunma özelliğini aktif et. 
analog_3.enable_reporting() # 3 numaralı pinin okunma özelliğini aktif et. 

Data=[]
say=0
sure=0 
dt=0.1
while True: # Sonsuz bir döngü oluştur 
    say+=1
    sure=sure+dt
    value_0=analog_0.read() # Pin değerini oku 
    value_3=analog_3.read() # Pin değerini oku 
    led_3.write(value_0)
    led_6.write(value_3)
    print(say,value_0,value_3) # sıra numarası ve pin değerini ekrana yaz. 
    Data.append([sure,value_0,value_3])

    if keyboard.is_pressed('esc'):
        break
    t.sleep(dt)

led_3.write(value_0) # led 3 ü kapat 
led_6.write(value_3) # Led 6 yı kapat 
board.exit() # Port bağlantısını kes 

# grafik olarak çiz 
fig = plt.figure()
ax = fig.add_subplot(111) #♦  projection='3d'
np_Data=np.array(Data)
ax.plot(np_Data[:,0],np_Data[:,1])
ax.plot(np_Data[:,0],np_Data[:,2])
ax.set_xlabel('t')
ax.set_ylabel('A')
ax.legend(['A0','A3'])



    
    
    
    
    
    
    