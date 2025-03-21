# Problem 1

Fizikte, bir nesnenin sabit ivmeyle hareket ederken son hızını 
(veya hızını) bulmak için aşağıdaki denklem kullanılabilir:
```
vf = vi + at
burada:
vf= son hız
vi= ilk hız
a= hızlanma
t= zaman
```
İlk hız, ivme ve zaman verildiğinde, son hızı döndürecek bir fonksiyon yazın.
# 1.Problemin Çözümünü Buraya Yazınız
def son_hiz(vi, a, t):
    vf= vi+a*t
    return vf

vi=20
a=2
t=3
sonuc=son_hiz(vi, a, t)
print(sonuc)
# Problem 2

1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.

Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır. Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).
# 2.Problemin Çözümünü Buraya Yazınız
def mukemmel(i):
    sum=0
    for x in range (1,i):
        if i%x==0:
            sum+=x
    return sum==i
for i in range (1,1001):
    if mukemmel(i):
        print(i)
        
# Problem 3

1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)

# 3.Problemin Çözümünü Buraya Yazınız
def pisagor_ucgenleri():
    for a in range(1, 101):
        for b in range(1, 101):
            c = (a**2 + b**2) ** 0.5
            if c == int(c):  # c tam sayı ise
                print(f"({a}, {b}, {int(c)})")
pisagor_ucgenleri()
def pisagor_ucgenleri():
    sonuc = []
    for a in range(1, 101):
        for b in range(1, 101):
            c = (a**2 + b**2) ** 0.5
            if c == int(c):
                sonuc.append((a, b, int(c)))
    return sonuc
ucgenler = pisagor_ucgenleri()
for ucgen in ucgenler:
    print(ucgen)
# Problem 4

Bir duvar boyamaya karar verdiniz. Boya kutusunun üzerindeki talimatta, 1 kutu boyanın 5 metrekarelik bir duvarı boyayabileceği yazıyor. Rastgele bir duvar yüksekliği ve genişliği verildiğinde, kaç kutu boya satın almanız gerektiğini hesaplayın.

kutu sayısı = (duvar yüksekliği * duvar genişliği) ÷ kutu başına kaplama.

örneğin Yükseklik = 2, Genişlik = 4, Kaplama = 5

kutu sayısı = (2 * 4) ÷ 5 = 1.6

Ancak bir kutu boyanın 0,6'sını satın alamayacağınız için, sonuç 2 kutuya yuvarlanmalıdır .

# 4.Problemin Çözümünü Buraya Yazınız
def boya_hesapla(yukseklik, genislik, kaplama):
    alan = yukseklik * genislik
    kutu_sayisi = alan / kaplama
    return kutu_sayisi

# Örnek kullanım
yukseklik = float(input("Duvar yüksekliğini girin (metre): "))
genislik = float(input("Duvar genişliğini girin (metre): "))
kaplama = 5

sonuc = boya_hesapla(yukseklik, genislik, kaplama)
print(f"Gerekli kutu sayısı: {sonuc}")
# Problem 5

Bir kelimedeki ünlü ve ünsüz harfleri sayan bir fonksiyon yazınız.
# 5.Problemin Çözümünü Buraya Yazınız
def harf_sayaci(kelime):
    unlu_harfler = "aeıioöuüAEIİOÖUÜ"
    unlu_sayisi = 0
    unsuz_sayisi = 0
    
    for harf in kelime:
        if harf.isalpha():  # Sadece harfleri kontrol edelim
            if harf in unlu_harfler:
                unlu_sayisi += 1
            else:
                unsuz_sayisi += 1
                
    return unlu_sayisi, unsuz_sayisi
kelime = input("Bir kelime girin: ")
unlu, unsuz = harf_sayaci(kelime)
print(f"Ünlü harf sayısı: {unlu}")
print(f"Ünsüz harf sayısı: {unsuz}")
# Problem 6

Verilen bir listeden çift sayıları yazdıran bir fonksiyon yazınız.

# 6.Problemin Çözümünü Buraya Yazınız

def cift_sayi(list):
    ciftlist=[]
    for x in list:
        if x%2==0:
            ciftlist.append(x)
    print(ciftlist)
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
cift_sayi(list)
# Problem 7

0'dan 10'a kadar olan sayıların toplamını hesaplayan özyinelemeli (Recursive Function) bir fonksiyon oluşturan bir fonksiyon yazınız.

Özyinelemeli (Recursive Function) bir işlev, kendini tekrar tekrar çağıran bir işlevdir.

# 7.Problemin Çözümünü Buraya Yazınız
def toplam(n):
    if n == 0:  
        return 0
    else:
        return n + toplam(n - 1)

sonuc = toplam(10)
print(f"0'dan 10'a kadar olan sayıların toplamı: {sonuc}")
