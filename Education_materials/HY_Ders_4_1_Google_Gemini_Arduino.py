import os
from google import genai
from google.genai.errors import APIError

# >>> API ANAHTARINIZI BURAYA GİRİN <<<
GEMINI_API_KEY = "AIzaSyDdFHVHFqX4kxqTO2FWxj-iDYFm40G9FVQ" # ANAHTARINIZ_BURAYA
# Anahtarınızı tırnak işaretleri (" ") içinde tutun.

def basit_gemini_sorgusu(soru):
    """
    Doğrudan kodda tanımlanan API anahtarını kullanarak bir soru sorar.
    """
    # 1. API Anahtarını Ayarlama (Client'a doğrudan verilir)
    if not GEMINI_API_KEY or GEMINI_API_KEY == "ANAHTARINIZ_BURAYA":
        return "HATA: Lütfen GEMINI_API_KEY değişkenine geçerli anahtarınızı girin."
    try:
        # Client oluşturulurken anahtar doğrudan kullanılır.
        client = genai.Client(api_key=GEMINI_API_KEY)
        print(f"Soru: {soru}")
        print("Model yanıtı bekleniyor...")
        # 2. Modeli Çağırma
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=soru,
        )

        # 3. Yanıtı Döndürme
        return response.text

    except APIError as e:
        return f"\n--- HATA ---\nAPI Anahtarı Geçersiz veya Bağlantı Sorunu Var: {e}"
    except Exception as e:
        return f"\n--- GENEL HATA ---\nBeklenmedik bir hata oluştu: {e}"

# --- KULLANIM ---
kullanici_sorusu = "Dünyadaki en büyük 5 okyanusun isimleri nelerdir?"

yanit = basit_gemini_sorgusu(kullanici_sorusu)

print("\n--- Gemini Yanıtı ---\n")
print(yanit)
print("\n" + "="*40)




# Sürekli sorgu 
import keyboard  # using module keyboard
say=0
while True: # Sonsuz bir döngü oluştur 
    say+=1
    print('\n\n\n---  sorgu :',say, '---\n') # sıra numarası ve pin değerini ekrana yaz. 
    Soru = input('Lütfen sorunuzu giriniz : ')
    yanit = basit_gemini_sorgusu(Soru)
    print(yanit)
    print("\n" + "="*40)

    
    if keyboard.is_pressed('esc'):
        break

5
