# Problem 1
Bir YetGenli yeni aldığı bahçesinin etrafına çit çevirmek istiyor. Bahçenin etrafını çit ile çevirmek için gerekli çit uzunluğunu ve bahçenin alanını hesaplayan fonksiyonu yazınız.
# 1.Problemin Çözümünü Buraya Yazınız
def bahce_hesapla(uzunluk, genislik):
    cevre = 2 * (uzunluk + genislik)
    alan = uzunluk * genislik
    print("Çevre:", cevre)
    print("Alan:", alan)
uzunluk = float(input("Bahçenin uzunluğunu girin (metre): "))
genislik = float(input("Bahçenin genişliğini girin (metre): "))
bahce_hesapla(uzunluk, genislik)
# Problem 2
Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.
# 2.Problemin Çözümünü Buraya Yazınız
def asalsayi(x):
    if
# Problem 3
YetGen liderlerinin kurdukları girişim unicorn oluyor. YetGen liderleri iş arkadaşlarının alacağı ücretlerini hesaplamak için bir fonksiyon yazdılar. Bu fonksiyonu kullanarak, YetGen liderlerinin iş arkadaşlarına verecekleri ücretleri hesaplayınız.

Ücret hesaplanması çalışma saatine bağlıdır. Bunun için kullanıcıdan çalışma saati bilgisinn alın. Sonrasında yapılacak ödemenin hesaplanacağı computePay() adlı bir fonksiyon oluşturun. Bu fonksiyonun içinde işlemler yapın. Çalışma saati 40 ve altındaysa saat başına ücret 10 TL’dir. 40 saatin üstünde çalışıldıysa saat başına ücret 15 TL sayılmaktadır.

```
Test etmek için 30 saat değerini giriniz,  sonuç 300 TL çıkmalı, 
ikincil test olarak 50 değerini giriniz,  sonuç 750 TL çıkmalı.
```
# 3.Problemin Çözümünü Buraya Yazınız
def computePay(saat):
    if saat <= 40:
        ucret = saat * 10
    elif saat>40:
        ucret = saat  * 15
    return ucret

saat = int(input("Çalışma saatini girin: "))
print(f"Ödenecek ücret: {computePay(saat)} TL")
# Problem 4
YetGenliler zirveye gitmek için toplanıyor. Zirveye gitmek için kiraladıkları araçlar 4'er kişiliktir. Gelecek kişi sayısı için Airtable üzerinde form açılıyor. Gelecek kişi sayısını alıp dört kişilik araçlara bölüp kalan kişi sayısını döndüren bir fonksiyon yazınız.
# 4.Problemin Çözümünü Buraya Yazınız
def kalan_kisi_sayisi(kisi_sayisi):
    kalan = kisi_sayisi % 4
    return kalan
kisi_sayisi = int(input("Gelecek kişi sayısını girin: "))
print(f"Kalan kişi sayısı: {kalan_kisi_sayisi(kisi_sayisi)}")
# Problem 5
sayiTopla() adında bir fonksiyon yazın. sayiTopla() fonksiyonu girilen sayıları toplayarak yazdırmasını sağlayan bir fonksiyon yazınız.

Örneğin sayiTopla(1,2,3,4,5) yazdığımızda 15 çıktısını almalıyız. sayiTopla(1,2,3,4,5,6,7,8,9,10) yazdığımızda 55 çıktısını almalıyız.
# 5.Problemin Çözümünü Buraya Yazınız

def sayiTopla(*x):
    toplam=0
    for i in x:
        toplam+=i
    print(toplam)
sayiTopla(1, 2, 3, 4, 5)
sayiTopla(1,2,3,4,5,6,7,8,9,10)

# Problem 6

[("xxx",1),("xxx",2),("xxx",9),("xxx",3), ("xxx",1),("xxx",13),("xxx",26),("xxx",4)] listesi içerisinde verilen elemanların her birini tuple içindeki 2. Elemana göre sıralayınız. 


# 6.Problemin Çözümünü Buraya Yazınız
# Problem 7
List comprehension kullanarak 1'den 100'e kadar olan sayılardan sadece çift sayıları bir listeye atmayı yapmayı çalışın.
sayilar = [x for x in range(1, 101) if x % 2 == 0]
print(sayilar)
# 7.Problemin Çözümünü Buraya Yazınız
liste=[]
for i in range(1,101):
    if i%2==0:
        liste.append(i)
print(liste)
