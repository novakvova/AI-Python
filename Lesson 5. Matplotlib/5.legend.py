import matplotlib.pyplot as plt
import numpy as np

data1 = np.array([1, 2, 3, 4, 5, 6])
data2 = np.array([2, 3, 2, 5, 4, 7])
data3 = np.array([1, 4, 2, 6, 3, 5])

fig, axes = plt.subplots(figsize=(5,2.7))

axes.plot(np.arange(len(data1)), data1, label='data1')
axes.plot(np.arange(len(data2)), data2, label='data2')
#d - це буде ромб
axes.plot(np.arange(len(data3)), data3, 'd', label='data3')

axes.set_xlabel('Номер елемента')
axes.set_ylabel('Значення')

axes.set_title("Порівнення наборів даних")

axes.legend()

axes.grid(True)
plt.show()

