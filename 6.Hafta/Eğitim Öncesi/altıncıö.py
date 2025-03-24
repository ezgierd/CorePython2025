# Problem 1
Elinizde bir dikdörtgenin kenarlarını ifade eden sayı çiftlerinin bulunduğu bir liste olsun.

     [(3,4),(10,3),(5,6),(1,9)]

Şimdi kenar uzunluklarına göre dikdörtgenin alanını hesaplayan bir fonksiyon yazın ve bu listenin her bir elemanına bu fonksiyonu uygulayarak ekrana şöyle bir liste yazdırın.

     [12, 30, 30, 9]

İpucu : map() fonksiyonunu kullanmaya çalışın.
# 1.Problemin Çözümünü Buraya Yazınız
def alan_hesapla(kenarlar):
    return kenarlar[0] * kenarlar[1]

dikdortgenler = [(3,4), (10,3), (5,6), (1,9)]
alanlar = list(map(alan_hesapla, dikdortgenler))
print(alanlar)
# Problem 2

Elinizden her bir elemanı 3'lü bir demet olan bir liste olsun.

 ```[(3,4,5),(6,8,10),(3,10,7)]```

Şimdi kenar uzunluklarına göre bu kenarların bir üçgen oluşturup oluşturmadığını döndüren bir fonksiyon yazın ve sadece üçgen oluşturan kenarları bulunduran listeyi ekrana yazdırın.

 ```[(3, 4, 5), (6, 8, 10)]```

İpucu: filter() fonksiyonunu kullanmaya çalışın.
# 2.Problemin Çözümünü Buraya Yazınız
def ucgen_mi(kenarlar):
    a, b, c = sorted(kenarlar)
    return a + b > c 

kenar_listesi = [(3,4,5), (6,8,10), (3,10,7)]
ucgenler = list(filter(ucgen_mi, kenar_listesi))

print(ucgenler)
# Problem 3
Elinizde aşağıdaki gibi bir liste bulunmaktadır.

```[1,2,3,4,5,6,7,8,9,10]```

Bu listenin içindeki çift sayıların toplamını ekrana yazdıran bir fonksiyon yazın.

İpucu: İlk önce filter() fonksiyonu ile çift sayıları ayıklayın. Daha sonra reduce() fonksiyonunu kullanın.
# 3.Problemin Çözümünü Buraya Yazınız
from functools import reduce


def cift_mi(sayi):
    return sayi % 2 == 0

def topla(x, y):
    return x + y

liste = [1,2,3,4,5,6,7,8,9,10]

cift_sayilar = list(filter(cift_mi, liste))

toplam = reduce(topla, cift_sayilar)

print(f"Çift sayıların toplamı: {toplam}")
# Problem 4

Elinizde isimlerin ve soyisimlerin bulunduğu iki tane liste bulunmaktadır.

    isimler -----> ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

    soyisimler -----> ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
    
Bu isimleri ve soyisimleri sırasıyla eşleştirin ve ekrana alt alta isimleri ve soyisimleri yazdırın.

İpucu: zip() fonksiyonunu kullanmaya kullanın.
# 4.Problemin Çözümünü Buraya Yazınız
isimler = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
soyisimler = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

eslesmis_isimler = zip(isimler, soyisimler)

for isim, soyisim in eslesmis_isimler:
    print(f"{isim} {soyisim}")
# Problem 5

İçerisinde yetgen, core, python2, programı, 2022, basic2 elemanları bulunan bir liste oluşturun.

Bu listenin içindeki stringlerden içinde sadece rakam bulunanları ekrana yazdırın. Bunu yaparken try, except bloklarını kullanmayı unutmayın.
# 5.Problemin Çözümünü Buraya Yazınız
liste = ["yetgen", "core", "python2", "programı", "2022", "basic2"]
for eleman in liste:
    try:
        sayi = int(eleman)
        print(sayi)
    except ValueError:
        pass
