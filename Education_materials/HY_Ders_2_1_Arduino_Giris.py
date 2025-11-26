# -*- coding: utf-8 -*-
"""
Ders 2 

Arduino giriş ve hatırlama 
https://pypi.org/project/pyFirmata/
"AttributeError: module 'inspect' has no attribute 'getargspec'"
Eğer yukarıda ki hatayı alıyorsan 

pyfirmata.py dosyasında 185. satırda yer alan ifadeyi şu şekilde değiştir
len_args = len(inspect.getfullargspec(func)[0])



board = Arduino('/dev/tty.usbserial-A6008rIF') # eğer linux veya macbook ise 
board = pyfirmata.ArduinoMega('COM3') # Mega ise bağlantı kodu böyle olmalı 
board = pyfirmata.Arduino('COM3') # 'COM3 seri portunda yer alan arduino ya bağlan 
board.exit() # Port bağlantısını kes 

# on-off
board.digital[6].write(1) # Dijital 6 pinini aç 
board.digital[6].write(0) # Dijital 6 pinini kapat

pin3 = board.get_pin('d:3:o') # D3 pinini dijital çıkış olarak ayarla 
pin6 = board.get_pin('d:6:p') # D6 pinini PWM çıkış olarak ayarla 

analog_0 = board.get_pin('a:0:i') # 0 numaralı pini analog giriş olarak ayarla
pin12 = board.get_pin('d:12:i') # 12 numaralı pini giriş olarak ayarla

iterator = pyfirmata.util.Iterator(board) # Sürekli olarak pin verilerini kontrol edecek bir iteratör tanımla 
iterator.start() # İteratörü çalıştır 
pin12.enable_reporting() # 12 numaralı pinin okunma özelliğini aktif et. 

"""

import pyfirmata # firmata kütüphanesini yüklüyoruz
import time as time

# board = Arduino('/dev/tty.usbserial-A6008rIF') # eğer linux veya macbook ise 
# board = pyfirmata.ArduinoMega('COM3') # Mega ise bağlantı kodu böyle olmalı 
board = pyfirmata.Arduino('COM3') # 'COM3 seri portunda yer alan arduino ya bağlan 
print('Arduino bağlantısı kuruldu ..') # Ekrana bağlandığını yaz. 

board.exit() # Port bağlantısını kes 
print('Arduino bağlantısı kesildi ..') # Ekrana bağlandığını yaz. 



## Digital Pin açma kapatma 
port='COM3'
board = pyfirmata.Arduino(port) # 'COM3 seri portunda yer alan arduino ya bağlan 
print(port,'Arduino bağlantısı kuruldu ..') # Ekrana bağlandığını yaz. 

board.digital[6].write(1) # Dijital 6 pinini aç 
time.sleep(0.5) # 0.5 saniye bekle
board.digital[6].write(0) # Dijital 6 pinini kapat 
time.sleep(0.5) # 0.5 saniye bekle

board.exit() # Port bağlantısını kes 
print('Arduino bağlantısı kesildi ..') # Ekrana bağlandığını yaz. 


# 5 defa aynı pini çalıştırma 
port='COM3'
board = pyfirmata.Arduino(port) # 'COM3 seri portunda yer alan arduino ya bağlan 
print(port,'Arduino bağlantısı kuruldu ..') # Ekrana bağlandığını yaz. 

for i in range(5):
    print ('i=',i)
    board.digital[6].write(1) # Dijital 6 pinini aç 
    time.sleep(0.5) # 0.5 saniye bekle
    board.digital[6].write(0) # Dijital 6 pinini kapat 
    time.sleep(0.5) # 0.5 saniye bekle

board.exit() # Port bağlantısını kes 
print('Arduino bağlantısı kesildi ..') # Ekrana bağlandığını yaz. 


# Listede bulunan pinleri çalıştırma
port='COM3'
board = pyfirmata.Arduino(port) # 'COM3 seri portunda yer alan arduino ya bağlan 
print(port,'Arduino bağlantısı kuruldu ..') # Ekrana bağlandığını yaz. 

pin_list=[3,6,9,10,11]
for pin in pin_list:
    print ('i=',pin)
    board.digital[pin].write(1) # Dijital 6 pinini aç 
    time.sleep(0.5) # 0.5 saniye bekle
    board.digital[pin].write(0) # Dijital 6 pinini kapat 
    time.sleep(0.5) # 0.5 saniye bekle

board.exit() # Port bağlantısını kes 
print('Arduino bağlantısı kesildi ..') # Ekrana bağlandığını yaz. 




"""

"""