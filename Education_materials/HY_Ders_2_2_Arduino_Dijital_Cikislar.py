"""
Ders 2.2  

Arduino giriş pin kullanımı 

"""

import pyfirmata # firmata kütüphanesini yüklüyoruz
import time as t

# Pinleri değişken olarak atama 
port='COM3'
board = pyfirmata.Arduino(port) # 'COM3 seri portunda yer alan arduino ya bağlan 
print(port,'Arduino bağlantısı kuruldu ..') # Ekrana bağlandığını yaz. 


pin3 = board.get_pin('d:3:o')
pin6 = board.get_pin('p:6:p')


# pin3.mode = pyfirmata.DIGITAL
pin3.write(1)
t.sleep(0.5) # 0.5 saniye bekle
pin3.write(0)

# pin6.mode = pyfirmata.PWM
pin6.write(1.0)
t.sleep(0.5) # 0.5 saniye bekle
pin6.write(0.75)
t.sleep(0.5) # 0.5 saniye bekle
pin6.write(0.5)
t.sleep(0.5) # 0.5 saniye bekle
pin6.write(0.25)
t.sleep(0.5) # 0.5 saniye bekle
pin6.write(0.0)

# Pin ışığını açıp kapatma 
for i in range(5):
    pin6.write(i*0.2)
    t.sleep(0.5) # 0.5 saniye bekle
for i in range(5):
    pin6.write(1-i*0.2)
    t.sleep(0.5) # 0.5 saniye bekle

board.exit() # Port bağlantısını kes 



# Uygulama 1 Soru sorma ve doğru ise led kontrol 
port='COM3'
board = pyfirmata.Arduino(port) # 'COM3 seri portunda yer alan arduino ya bağlan 
print(port,'Arduino bağlantısı kuruldu ..') # Ekrana bağlandığını yaz. 

pin_dogru = board.get_pin('d:6:o')
pin_yanlis = board.get_pin('d:3:o')

sonuc = input('6 + 7 =')
if int(sonuc)==(6+7):
    pin_dogru.write(1)
else: 
    pin_yanlis.write(1)

t.sleep(2) # 0.5 saniye bekle
pin_yanlis.write(0)
pin_dogru.write(0)

board.exit() # Port bağlantısını kes 




# Uygulama 1 Soru sorma ve doğru ise led kontrol 
import pyfirmata # firmata kütüphanesini yüklüyoruz
import time as t
import numpy as np
port='COM3'
board = pyfirmata.Arduino(port) # 'COM3 seri portunda yer alan arduino ya bağlan 
print(port,'Arduino bağlantısı kuruldu ..') # Ekrana bağlandığını yaz. 

pin_dogru = board.get_pin('d:6:o')
pin_yanlis = board.get_pin('d:3:o')

a=np.random.randint(1,10)
b=np.random.randint(1,10)

print('Lütfen işlemin sonucunu giriniz. ')
sonuc = input(str(a)+'+'+str(b)+'=')
cevap=(a+b)
if int(sonuc)==cevap:
    pin_dogru.write(1)
    print('Tebrikler',a,'+',b,'=',sonuc)
else: 
    pin_yanlis.write(1)
    print('Olmadı',a,'+',b,'=',cevap,'olmalıydı')

t.sleep(2) # 0.5 saniye bekle
pin_yanlis.write(0)
pin_dogru.write(0)

board.exit() # Port bağlantısını kes 