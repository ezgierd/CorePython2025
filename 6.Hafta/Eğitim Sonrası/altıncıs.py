# Problem 1 
Bir sayının çift olup olmadığını sorgulayan bir fonksiyon yazın. Bu fonksiyon, eğer sayı çift ise bu değeri dönsün. Ancak sayı tek sayı ise fonksiyon raise ile ValueError hatası oluştursun. Daha sonra, içinde çift ve tek sayılar bulunduran bir liste tanımlayın ve liste üzerinde gezinerek ekrana sadece çift sayıları bastırın.
# 1.Problemin Çözümünü Buraya Yazınız
def cift_mi(sayi):
    if sayi % 2 == 0:
        return sayi
    else:
        raise ValueError("Bu sayı tek.")
sayilar = [2, 5, 8, 11, 14, 17, 20]
for s in sayilar:
    try:
        print(cift_mi(s))
    except ValueError:
        pass

# Problem 2

2 YetGen lideri ders sırasında canları sıkılınca oyun oynamak isterler. Ancak hangi oyunu oynayacaklarına karar veremezler ve son olarak kendi oyunlarını yazmaya karar verirler.
Liderlerimizin kodlamak istediği oyun kuralları şöyledir:
- Oyunda random olarak 0 ile 100 arasında bir sayı tutulur.
- Kullanıcıdan bilgisayarın tuttuğu sayıyı tahmin etmesi için bir sayı girmesini istenir.
- Eğer kullanıcının girdiği sayı bulunması gereken sayıdan küçükse  tahmininizi yükseltin, büyükse tahmininizi düşürün şeklinde bir çıktı verilir.
- Oyunun gerçeğe yakın olması için bilgisayarın çalışmasını simgelemek için 1 saniye bekleme süresi tanınır.
- Kullanıcı 5 hakkı vardır. 5 hakkı da kullanıp sayıyı bulamazsa oyunu kaybeder.
# 2.Problemin Çözümünü Buraya Yazınız
import random
import time

def sayi_tahmin_oyunu():
    print("Tahmin oyununa hoş geldiniz!")
    gizli_sayi = random.randint(0, 100)
    tahmin_hak = 5

    while tahmin_hak > 0:
        try:
            tahmin = int(input(f"\n{tahmin_hak} hakkınız kaldı. Bir sayı tahmin edin (0-100): "))
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")
            continue

        time.sleep(1)  # Bilgisayar düşünüyormuş gibi 1 saniye bekle

        if tahmin == gizli_sayi:
            print("Tebrikler! Sayıyı doğru tahmin ettiniz 🎉")
            break
        elif tahmin < gizli_sayi:
            print("Tahmininizi yükseltin.")
        else:
            print("Tahmininizi düşürün.")

        tahmin_hak -= 1

    if tahmin_hak == 0 and tahmin != gizli_sayi:
        print(f"Üzgünüm, hakkınız bitti. Doğru sayı {gizli_sayi} idi.")

sayi_tahmin_oyunu()
