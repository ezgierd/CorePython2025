# Problem 1 
Kullanıcıdan aldığı ürün bilgisini (ad, fiyat) urunler.txt dosyasına kayıt eden fonksiyonu yazınız.
# 1.Problemin Çözümünü Buraya Yazınız
def urun_kaydet():
    ad = input("Ürün adını girin: ")
    fiyat = input("Ürün fiyatını girin: ")

    dosya = open("urunler.txt", "a", encoding="utf-8")
    dosya.write(ad + "," + fiyat + "\n")
    dosya.close()

    print("Ürün başarıyla kaydedildi.")

urun_kaydet()
# Problem 2
1.problemde oluşturulan text dosyası içerisinde kullanıcıdan alacağımız eski kelime isimli değişkene atadığımız 
ve değiştirilmesini istediğimiz kelimemizi yerini alıcak olan yeni kelime isimli değişkene atayın. Belirlenen kelimeleri text dosyasında değiştiren fonksiyonu yazınız.
# 2.Problemin Çözümünü Buraya Yazınız
def kelime_degistir():
    eski_kelime = input("Değiştirmek istediğiniz kelime: ")
    yeni_kelime = input("Yeni kelime: ")

    # Dosyayı okuyup içeriği al
    dosya = open("urunler.txt", "r", encoding="utf-8")
    icerik = dosya.read()
    dosya.close()

    # Kelimeyi değiştir
    yeni_icerik = icerik.replace(eski_kelime, yeni_kelime)

    # Yeni içerikle dosyayı yeniden yaz
    dosya = open("urunler.txt", "w", encoding="utf-8")
    dosya.write(yeni_icerik)
    dosya.close()

    print("Kelime başarıyla değiştirildi.")

# Fonksiyonu çağır
kelime_degistir()
# Problem 3
Vehicle sınıfının tüm değişkenlerini ve yöntemlerini devralacak bir alt sınıf olarak Bus sınıfı oluşturunuz.



```
Output
> Name: School Volvo Speed: 180 Mileage: 12
```

# 3.Problemin Çözümünü Buraya Yazınız
class Vehicle:
    def __init__(self, name, speed, mileage):
        self.name = name
        self.speed = speed
        self.mileage = mileage

    def display_info(self):
        print(f"Name: {self.name} Speed: {self.speed} Mileage: {self.mileage}")

class Bus(Vehicle):
    pass  
school_bus = Bus("Mercedes", 280, 15)
school_bus.display_info()
