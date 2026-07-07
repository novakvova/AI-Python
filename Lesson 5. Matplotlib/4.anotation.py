import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(figsize=(5,2.7))

t = np.arange(0.0,5.0,0.01)
#y = cos(2πt)
s = np.cos(2*np.pi*t)

#Будуємо графік для косинуса
# lw - товщина ліній 2px
line, = axes.plot(t, s, lw=2)

#xy=(2,1), - точка на яку вказує стрілочка
#xytext - місце розташування тексту
#arrowprops - параметри стрілки

axes.annotate(
    'Локальний максимум',
    xy=(2,1),
    xytext=(3,1.5),
    arrowprops=dict(
        facecolor='black', # колір
        shrink=0.05, # Скорочення довжина на 5%
    )
)

# Ставимо мері для осей
axes.set_ylim(-2,2)

axes.set_xlabel("Час")
axes.set_ylabel("Значення cos(x)")
axes.set_title("Графік функції косинуса")
axes.grid(True)

plt.show()