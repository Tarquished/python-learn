import numpy as np

# numpy adalah module di python, dan fungsinya untuk memproses data dengan lebih cepat dibandingkan dengan array python biasa
#numpy lebih cepat dari python biasa karena dia memprosesnya berbeda, jika python biasa itu overhead, kalau numpy itu beda deh pokoknya
#kalau array itu data yang udah jadi, kalau vektor list masih cuma data mentahnya doang
# shape itu untuk liat ukuran dari matriksnya, bisa 3x3 atau 2x2 atau 2x3 dll

array = np.random.randint(0,11,size = (3,5))
print(array.shape)
