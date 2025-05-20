# 1 - numpy kütüphanesini import edin

# 2 - 0 ile 10 arasında 5 sayıdan oluşan matris üretin

# 3 - matris'in boyutunu öğrenin

# 4 - matris'i yeniden boyutlandırın

# 5 - matris'in boyut sayısını öğrenin


import numpy as np

matris = np.random.randint(0, 10, size=5)
print("Matris:", matris)

print("Matrisin şekli (boyutu):", matris.shape)

matris_reshape = matris.reshape((5, 1))
print("Yeniden boyutlandırılmış matris:\n", matris_reshape)

print("Matrisin boyut sayısı:", matris_reshape.ndim)



# 1 - 0 ile 10 arasında bulunan tek sayılardan oluşan matris üretin

# 2 - Oluşturduğunuz matrisi parçalayın

# 3 - Parçalanmış matrisleri birleştirin

import numpy as np
tek_sayilar = np.arange(1, 10, 2)  
print("Tek sayılardan oluşan matris:", tek_sayilar)
parca1, parca2 = np.array_split(tek_sayilar, 2)
print("Parça 1:", parca1)
print("Parça 2:", parca2)

birlesik = np.concatenate((parca1, parca2))
print("Birleştirilmiş matris:", birlesik)

# 1 - 5 ile 100 arasında ikişer ikişer atlayarak rastgele 10 sayıdan oluşan matris üretin

# 2 - matris'in özelliklerini inceleyin


import numpy as np
sayilar = np.arange(5, 101, 2)  
matris = np.random.choice(sayilar, size=10, replace=False)  
print("Rastgele matris:", matris)


print("Matrisin tipi:", type(matris))
print("Matrisin veri tipi:", matris.dtype)
print("Matrisin boyutu (shape):", matris.shape)
print("Matrisin boyut sayısı (ndim):", matris.ndim)
print("Matrisin eleman sayısı (size):", matris.size)
print("Matrisin maksimum değeri:", matris.max())
print("Matrisin minimum değeri:", matris.min())
print("Matrisin ortalaması:", matris.mean())


