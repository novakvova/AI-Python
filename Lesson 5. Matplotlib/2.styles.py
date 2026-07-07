import matplotlib.pyplot as plt
import numpy as np

#Розподіл від 0 до 2
x = np.linspace(0,2,100)

#Фігура та область
#figsize - розмір фігури у дюймах
#layout - constrained - автоматично відбуваються відступи між елементами
fig, axes = plt.subplots(figsize=(5,2.7), layout='constrained')

#Лінійна функція - y=x
axes.plot(x, x, label='Лінійна')
#Кваратична фукнція
axes.plot(x,x**2,label="Квадратична")
#Кубічна функція
axes.plot(x,x**3,label="Кубічна")
#Додаємо підписи осей
axes.set_xlabel('Х значення')
axes.set_ylabel('Y значення')
#Заголовок графіку
axes.set_title("Відображення графіків")
axes.legend() # Відобразити параметри label на графіку
# Відобразити вікно із графіком
plt.show()