# -*- coding: utf-8 -*-
"""
Ders 1 

Python giriş ve hatırlama 
"""


# Ekrana yazı yazma 
print("Merhaba")


# String türünde değişkenler ve yazdırma 
ad="Mehmet Ali" 
soyad ="Büyük"
print("Merhaba "+ad+" "+soyad)
print("Merhaba",ad,soyad)


# Temel Değişkenler 
sayi_1=1            # (integer)     Tam sayı  
sayi_2=2.0          # (float)       Reel sayı (virgüllü sayılar)
sayi_3=[1,2.0]      # (list)        liste Birden fazla türü aynı anda depolayabilir 
sayi_4=[[1,2.0],
        [5.0,3.0]]      # (list)        liste Birden fazla türü aynı anda depolayabilir 
#sayi_4=(1,2.0)      # (tuple)       yığın Özel bir listeleme türü  

print(sayi_1,sayi_2,sayi_3[0],sayi_4[1])
print(sayi_4[0],sayi_4[1])
print(sayi_4[0][1],sayi_4[1][0])


# Kullanıcıdan veri alma 
Girdi = input('Adınızı giriniz : ')
print('Merhaba, ' + Girdi)

#-
Girdi_1 = input('Adınızı giriniz : ')
Girdi_2 = input('Soyadınızı giriniz : ')
print('Merhaba, ' + Girdi_1+' '+Girdi_2)

# çoklu giriş
x, y, z = input("Sayılar: ").split()
print(x)
print(y)
print(z)


# Koşullu ifade 
Girdi = input('Adınızı giriniz : ')
if (Girdi=="Hüseyin"):
    print('Merhaba, ' + Girdi)
    print('Başarı ile giriş yaptınız...')
else: 
    print('Hatalı giriş...')

#-
Girdi = input('Adınızı giriniz : ')
if (Girdi=="Hüseyin"):
    print('Merhaba, ' + Girdi)
    print('Başarı ile giriş yaptınız...')
elif (Girdi=='Ali'):
    print('Merhaba, ' + Girdi+' bey sizi bekliyorduk')
else: 
    print('Hatalı giriş...')



# For döngüsü 
for i in range(10): 
    print(i)
    
 #-   
for i in range(2,5):
    print(i)
    
  #-     
Meyveler=['elma','armut','ayva']
for i in range(len(Meyveler)):
    print(i,'. meyve',Meyveler[i])

for meyve in Meyveler:
    print(meyve)
    
    
for i in range(2,5):
    for j in range(6,15):
        print(i,j)
    
# İki sayıyı topla 
x, y = input("Sayılar: ").split()
toplam=x+y 
print(x,'+',y,'=',toplam)

x, y = input("Sayılar: ").split()
toplam=int(x)+int(y) 
print(x,'+',y,'=',toplam)

x, y = input("Sayılar: ").split()
toplam=float(x)+float(y) 
print(x,'+',y,'=',toplam)

# Hesap makinesi 
x,isaret, y = input("işlemi giriniz: ").split()
if isaret=='+':
    toplam=float(x)+float(y)
    print(x,isaret,y,'=',toplam)
elif isaret=='-':
    toplam=float(x)-float(y)
    print(x,isaret,y,'=',toplam)
elif isaret=='*':
    toplam=float(x)*float(y)
    print(x,isaret,y,'=',toplam)
elif isaret=='/':
    toplam=float(x)+float(y)
    print(x,isaret,y,'/',toplam)
else: 
    print('Hatalı giriş yaptınız')    
    

# a dan b ye kadar olan sayıların toplamı 
a, b = input("a ve b sayılarını giriniz: ").split()
toplam=0 
a=int(a);  b=int(b)
for i in range (a+1,b):
    toplam =toplam+i 
    print('    i=',i,toplam)
print(a,' ile ',b,' arasında ki sayıların toplamı')


# Faktöryel hesabı 
sayi = input('Bir sayı giriniz : ')
carpim=1.0 
for i in range(1,int(sayi)+1):
    carpim=carpim*i
print(sayi,'! = ',carpim)
print(str(sayi)+'! = '+str(carpim))

    
    
    
    
    
