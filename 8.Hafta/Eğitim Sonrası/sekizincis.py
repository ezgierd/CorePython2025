# Problem 1

Şimdi beraber kullanıcılardan aldığımız verileri işleyerek, onlara hem çıktı verecek, hem de aldığımız ve hesapladığımız verileri ileride kullanabilmek adına kaydedeceğiz.


 **Bu bir veri giriş platformu olacak**


 * kullanıcıya kaç giriş yapacağını soracağız
* kullanıcıdan isim-soyisim, yaş, boy, kilo bilgilerini alarak VKİ hesaplayacağız
* ardından bunları sınıflara göre kaydedeceğiz bir dosyaya kaydedeceğiz


Sınıflar ise şu şekilde: 
* 18, 5 kg/m.'nin altında olanlar: Zayıf
* 18.5 – 24, 9 kg/m. arasında olanlar: Normal kilolu
* 25 – 29, 9 kg/m. arasında olanlar: Fazla kilolu
* 30 – 39, 9 kg/m. arasında olanlar: Obez
* 40 kg/m.'nin üzerinde olanlar: İleri derecede obez (morbid obez), olarak görülür.
# 1.Problemin Çözümünü Buraya Yazınız
import csv

def vki_hesapla(kilo, boy):
    return kilo / (boy ** 2)

def vki_sinifi(vki):
    if vki < 18.5:
        return "Zayıf"
    elif 18.5 <= vki < 25:
        return "Normal kilolu"
    elif 25 <= vki < 30:
        return "Fazla kilolu"
    elif 30 <= vki < 40:
        return "Obez"
    else:
        return "İleri derecede obez"
def veri_girisi():
    kisi_sayisi = int(input("Kaç kişi için veri girişi yapacaksınız? "))
    bilgiler = []

    for i in range(kisi_sayisi):
        print(f"\n{i+1}. kişi bilgileri:")
        ad = input("Ad: ")
        soyad = input("Soyad: ")
        yas = int(input("Yaş: "))
        boy = float(input("Boy (metre): "))
        kilo = float(input("Kilo (kg): "))
        
        vki = vki_hesapla(kilo, boy)
        sinif = vki_sinifi(vki)
        print(f"{ad} {soyad} için VKİ: {vki:.2f} - {sinif}")

        bilgiler.append([ad, soyad, yas, boy, kilo, round(vki, 2), sinif])

    return bilgiler
def dosyaya_yaz(veriler, dosya_adi="vki_kayitlari.csv"):
    with open(dosya_adi, mode="w", newline="", encoding="utf-8") as dosya:
        yazici = csv.writer(dosya)
        yazici.writerow(["Ad", "Soyad", "Yaş", "Boy (m)", "Kilo (kg)", "VKİ", "Sınıf"])
        yazici.writerows(veriler)
    print(f"\nVeriler '{dosya_adi}' dosyasına kaydedildi.")
def calistir():
    veriler = veri_girisi()
    dosyaya_yaz(veriler)
calistir()
# Problem 2
**YetBar - Smoothie Bank**
---
YetBar spor salonunun girişinde bulunan, insansız bir sağlıklı içecek otomatıdır. Kullanıcı çeşitli girdiler smoothie içeceğine koyacağı ürünleri belirleyebilir, fiyat hesaplaması yaptırabilir ya da sadece menüyü görüntüleyebilir.

**Projenin Amacı:**

*   Birbirini etkileyen ve bir kod içerisinde birden fazla defa başvurulacak fonksiyonların oluşturulup, "fonksiyonel" proglamlamak.
*   Büyük programları yazarken, yazılımcı olarak yapabileceğimiz hatalardan kaçınmak için kontrol yöntemleri geliştirmek.
*   Kullanıcı inputlarını ve yaptığımız hesapları, raporlamak/loglamak amacıyla kaydetmek.

**Programdan Beklenen Çıktılar**
* Program kullanıcıya temelde 2 farklı işlem yapma imkanı sağlar.
> 1. Menüyü görüntüleme
> 3. Satın alma
* Satın alınan her içecek tarih, fiyat bilgisi ile kaydedilmeli ve her zaman ulaşılabilir olmalıdır.



# 2.Problemin Çözümünü Buraya Yazınız
import datetime
import csv
MENU = {
    "Muz": 15,
    "Çilek": 20,
    "Yulaf": 12,
    "Protein Tozu": 25,
    "Süt": 8,
    "Badem Sütü": 10
}

# Kullanıcı siparişlerini logladığımız dosya
LOG_DOSYA = "smoothie_log.csv"

# Fonksiyon: Menüyü ekrana yazdır
def menu_goster():
    print("\n--- SMOOTHIE MENÜSÜ ---")
    for malzeme, fiyat in MENU.items():
        print(f"{malzeme}: {fiyat} TL")
    print("------------------------\n")

# Fonksiyon: Kullanıcıdan smoothie içeriği al, fiyat hesapla
def satin_al():
    sepet = []
    toplam_fiyat = 0

    print("\nSmoothie’nize eklemek istediğiniz malzemeleri yazın. İşiniz bittiğinde 'bitir' yazın.\n")

    while True:
        secim = input("Malzeme adı (ya da 'bitir'): ").strip().title()
        
        if secim == "Bitir":
            break
        elif secim in MENU:
            sepet.append(secim)
            toplam_fiyat += MENU[secim]
            print(f"✓ {secim} eklendi. Ara toplam: {toplam_fiyat} TL")
        else:
            print("⚠ Bu malzeme menüde yok. Lütfen geçerli bir isim girin.")

    if not sepet:
        print("❗ Herhangi bir malzeme seçilmedi. Sipariş iptal edildi.")
        return

    print("\n✅ Sipariş Özeti:")
    for malzeme in sepet:
        print(f"- {malzeme} ({MENU[malzeme]} TL)")
    print(f"Toplam Tutar: {toplam_fiyat} TL")

    log_kaydet(sepet, toplam_fiyat)

# Fonksiyon: Siparişi log dosyasına kaydet
def log_kaydet(malzeme_listesi, fiyat):
    tarih = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(LOG_DOSYA, mode="a", newline="", encoding="utf-8") as dosya:
        yazici = csv.writer(dosya)
        yazici.writerow([tarih, ", ".join(malzeme_listesi), fiyat])
    
    print(f"🗂 Sipariş {LOG_DOSYA} dosyasına kaydedildi.")

# Fonksiyon: Kullanıcı arayüzünü başlat
def baslat():
    print("☀ Hoş geldiniz! YetBar Smoothie Otomatı başlatılıyor...\n")

    while True:
        print("1 - Menüyü Görüntüle")
        print("2 - Smoothie Satın Al")
        print("3 - Çıkış\n")

        secim = input("Seçiminiz (1/2/3): ").strip()

        if secim == "1":
            menu_goster()
        elif secim == "2":
            menu_goster()
            satin_al()
        elif secim == "3":
            print("👋 Sağlıklı günler dileriz!")
            break
        else:
            print("⚠ Geçersiz seçim! Lütfen 1, 2 veya 3 girin.\n")

# Programı başlat
baslat()
