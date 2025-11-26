# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 21:42:45 2025

@author: HY
"""


import pyfirmata # firmata kütüphanesini yüklüyoruz
import time as t
import keyboard  # using module keyboard
# Pinleri değişken olarak atama 


# Dijital sinyal okuma 
port='COM3'
board = pyfirmata.Arduino(port) # 'COM3 seri portunda yer alan arduino ya bağlan 
print(port,'Arduino bağlantısı kuruldu ..') # Ekrana bağlandığını yaz. 

pin12 = board.get_pin('d:12:i') # 12 numaralı pini 
iterator = pyfirmata.util.Iterator(board) # Sürekli olarak pin verilerini kontrol edecek bir iteratör tanımla 
iterator.start() # İteratörü çalıştır 
pin12.enable_reporting() # 12 numaralı pinin okunma özelliğini aktif et. 

say=0
while True: # Sonsuz bir döngü oluştur 
    say+=1
    pin_value=pin12.read() # Pin değerini oku 
    print(say,pin_value) # sıra numarası ve pin değerini ekrana yaz. 
    if keyboard.is_pressed('esc'):
        break
    t.sleep(0.1)
board.exit() # Port bağlantısını kes 







# Dijital sinyal okuma 
port='COM3'
board = pyfirmata.Arduino(port) # 'COM3 seri portunda yer alan arduino ya bağlan 
print(port,'Arduino bağlantısı kuruldu ..') # Ekrana bağlandığını yaz. 

pin12 = board.get_pin('d:12:i') # 12 numaralı pini giriş olarak ayarla
iterator = pyfirmata.util.Iterator(board) # Sürekli olarak pin verilerini kontrol edecek bir iteratör tanımla 
iterator.start() # İteratörü çalıştır 
pin12.enable_reporting() # 12 numaralı pinin okunma özelliğini aktif et. 

isWork=True # 

t0=t.time() # zaman damgasını oku 
say=0
while isWork: # Sonsuz bir döngü oluştur 
    say+=1
    pin_value=pin12.read()
    print(say,pin_value)
    
    if pin_value==False: 
        isWork=False #
        print("program durduruldu")
    if keyboard.is_pressed('esc'):
        break
    t.sleep(0.1)
dt=t.time()-t0
print('işlem süresi : ',dt)

board.exit() # Port bağlantısını kes 







# Dijital sinyal okuma 
port='COM3'
board = pyfirmata.Arduino(port) # 'COM3 seri portunda yer alan arduino ya bağlan 
print(port,'Arduino bağlantısı kuruldu ..') # Ekrana bağlandığını yaz. 

pin2 = board.get_pin('d:2:i') # 2 numaralı pini giriş olarak ayarla
pin8 = board.get_pin('d:8:i') # 8 numaralı pini giriş olarak ayarla
pin12 = board.get_pin('d:12:i') # 12 numaralı pini giriş olarak ayarla
pinler=[pin2,pin8,pin12] # Pinleri bir listeye koy 

led3 = board.get_pin('d:3:o') # 6 numaralı pini çıkış olarak ayarla
led6 = board.get_pin('d:6:o') # 6 numaralı pini çıkış olarak ayarla
led10 = board.get_pin('d:10:o') # 9 numaralı pini çıkış olarak ayarla
ledler=[led3,led6,led10] # Ledleri bir listeye koy 

iterator = pyfirmata.util.Iterator(board) # Sürekli olarak pin verilerini kontrol edecek bir iteratör tanımla 
iterator.start() # İteratörü çalıştır 

for pin in pinler: #Pinleri okunabilir olarak ayarla 
    pin.enable_reporting() #  pinin okunma özelliğini aktif et. 

for led in ledler: #ledlerin tümünü sıra ile kapat 
    led.write(0.0) #  
    
isWork=True # 

t0=t.time() # zaman damgasını oku 
say=0
while isWork: # Sonsuz bir döngü oluştur 
    say+=1 # say 
    values=[] # boş bir liste oluştur 
    for pin in pinler:  # her pini incele 
        value=pin.read() # pin değerini oku 
        values.append(value) # okunan değeri listeye yaz 
        index=pinler.index(pin)# sıradaki pin indexini öğren 
        if value==False: 
            ledler[index].write(1.0)
        else: 
            ledler[index].write(0.0)
    print(say,values)
    
        
    if keyboard.is_pressed('esc'):
        break
    t.sleep(0.1)
dt=t.time()-t0
print('işlem süresi : ',dt)

for led in ledler: #ledlerin tümünü sıra ile kapat 
    led.write(0.0) #  
board.exit() # Port bağlantısını kes 





"""

while isWork:
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
    
    
    
    
    
    
    
    
    