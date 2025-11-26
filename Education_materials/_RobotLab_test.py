# -*- coding: utf-8 -*-
"""
ROBOLAB TEST 

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

out_pins=[3,6,9,10,11,5]
in_pins=[2,8,12,13]
Buttons=[]
Leds=[]
for i in out_pins:#range(2,12):#
    line='d:'+str(i)+':o'
    led = board.get_pin(line) # 0 numaralı pini analog giriş olarak ayarla
    print("pin : ",i)
    Leds.append(led)
    led.write(1)
    t.sleep(1)
    led.write(0)
    t.sleep(1)



iterator = pyfirmata.util.Iterator(board) # Sürekli olarak pin verilerini kontrol edecek bir iteratör tanımla 
iterator.start() # İteratörü çalıştır 
analog_0.enable_reporting() # 0 numaralı pinin okunma özelliğini aktif et. 
for i in in_pins:
    line='d:'+str(i)+':i'
    btn = board.get_pin(line) # 0 numaralı pini analog giriş olarak ayarla
    btn.enable_reporting()
    Buttons.append(btn)
say=0
while True: # Sonsuz bir döngü oluştur 
    say+=1
    value_0=analog_0.read() # Pin değerini oku 
    line=str(value_0)
    say=0
    for btn in Buttons:
        if btn.read()==False:
            Leds[say].write(1)
            t.sleep(2)
        else:
            Leds[say].write(0)
        line=line+" " +str(btn.read())
        say+=1
    print(say,line) # sıra numarası ve pin değerini ekrana yaz. 
    if keyboard.is_pressed('esc'):
        break
    t.sleep(0.1)
board.exit() # Port bağlantısını kes 
