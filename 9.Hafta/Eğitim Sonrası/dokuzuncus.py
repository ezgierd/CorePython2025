# Problem 1

Kumanda isminde bir sınıf oluşturarak aşağıdaki işlemleri yapmasını sağlayan fonksiyonları sınıf içerisinde yazalım.
1. Tv Aç
2. Tv Kapat
3. Ses Ayarları
4. Kanal Ekle
5. Kanal Sayısını Öğrenme
6. Rastgele Kanala Geçme
7. Televizyon Bilgileri


Kumandayı kapatmak için q tuşuna basılmalı ve diğer durumlarda hangi işlemi yapmak istediği sorulmalıdır. Her işlemde gerekli fonksiyonunun sınıf içerisinden çağırılması gerekmektedir.

random ve time kütüphanesini araştırarak kullanabilirsiniz.

Kendi istediğiniz özellikleri eklemekte serbetsiniz.
# 1.Problemin Çözümünü Buraya Yazınız
import random
import time
class Kumanda:
    def __init__(self, tv_durum="Kapalı", tv_ses=10, kanal_listesi=["TRT"], suanki_kanal="TRT"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.suanki_kanal = suanki_kanal

    # TV'yi açma 
    def tv_ac(self):
        if self.tv_durum == "Açık":
            print("TV zaten açık.")
        else:
            print("TV açılıyor")
            time.sleep(1)
            self.tv_durum = "Açık"
            print("TV açık.")

    # TV'yi kapatma 
    def tv_kapat(self):
        if self.tv_durum == "Kapalı":
            print("TV zaten kapalı.")
        else:
            print("TV kapatılıyor")
            time.sleep(1)
            self.tv_durum = "Kapalı"
            print("TV kapalı.")

    # Ses ayarlama 
    def ses_ayar(self):
        while True:
            islem = input("Sesi açmak için '+', kısmak için '-', çıkmak için 'q' tuşuna basın: ")
            if islem == "+":
                if self.tv_ses < 100:
                    self.tv_ses += 1
                    print(f"Ses: {self.tv_ses}")
                else:
                    print("Ses zaten maksimum")
            elif islem == "-":
                if self.tv_ses > 0:
                    self.tv_ses -= 1
                    print(f"Ses: {self.tv_ses}")
                else:
                    print("Ses zaten minimum!")
            elif islem == "q":
                print(f"Ses ayarı kapatıldı. Mevcut ses seviyesi: {self.tv_ses}")
                break
            else:
                print("Geçersiz tuşlama.")

    # Kanal ekleme 
    def kanal_ekle(self):
        yeni_kanal = input("Eklemek istediğiniz kanalın adını girin: ")
        print(f"{yeni_kanal} ekleniyor")
        time.sleep(1)
        self.kanal_listesi.append(yeni_kanal)
        print(f"{yeni_kanal} kanalı eklendi.")

    # Kanal sayısını öğrenme 
    def kanal_sayisi(self):
        print(f"Toplam {len(self.kanal_listesi)} kanal mevcut.")

    # Rastgele kanala geçme 
    def rastgele_kanal(self):
        self.suanki_kanal = random.choice(self.kanal_listesi)
        print(f"Şu anda {self.suanki_kanal} kanalındasınız.")

    # TV bilgilerini gösterme 
    def tv_bilgileri(self):
        print("\n--- TV Bilgileri ---")
        print(f"Durum: {self.tv_durum}")
        print(f"Ses: {self.tv_ses}")
        print(f"Kanallar: {self.kanal_listesi}")
        print(f"Şu Anki Kanal: {self.suanki_kanal}")
        print("---------------------\n")

kumanda = Kumanda()

print("Televizyon Kumandasına Hoşgeldiniz")

while True:
    print("\nYapmak istediğiniz işlemi seçiniz:")
    print("1 - TV Aç")
    print("2 - TV Kapat")
    print("3 - Ses Ayarları")
    print("4 - Kanal Ekle")
    print("5 - Kanal Sayısını Öğren")
    print("6 - Rastgele Kanala Geç")
    print("7 - TV Bilgilerini Görüntüle")
    print("q - Çıkış\n")

    islem = input("İşlem Seçiniz: ")

    if islem == "q":
        print("Kumanda kapatılıyor")
        break
    elif islem == "1":
        kumanda.tv_ac()
    elif islem == "2":
        kumanda.tv_kapat()
    elif islem == "3":
        kumanda.ses_ayar()
    elif islem == "4":
        kumanda.kanal_ekle()
    elif islem == "5":
        kumanda.kanal_sayisi()
    elif islem == "6":
        kumanda.rastgele_kanal()
    elif islem == "7":
        kumanda.tv_bilgileri()
    else:
        print("Lütfen tekrar deneyin.")
