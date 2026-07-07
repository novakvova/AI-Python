import matplotlib.pyplot as plt
import numpy as np

# середнє значення та стандартне відхилення
mu, sigma = 115, 15

#Генеруємо випадкові дані згідно вхідних параметрів
x = mu + sigma * np.random.randn(10000)

fig, axes = plt.subplots(figsize=(5,2.7), layout='constrained')

#Будуємо гістаграму на основі вхідни даних
#x - набір значення
#50 - кількість стовпчиків
#density - нормалізує гістограму до ймовірності
#alpha - прозорізорість стовпчиків
#facecolor - Колір стовпчиків
n,bins,patches = axes.hist(x, 50, density=True,
                           facecolor='C0', alpha=0.75)
axes.set_xlabel("Довжина [см]")
axes.set_ylabel("Ймовірність")

axes.set_title("Розподіл довжини\n(База)")


axes.text(75,0.025,r'$\mu=115,\sigma=15$')

axes.axis([55, 175, 0, 0.035])

plt.show() # Малюю гістаграму