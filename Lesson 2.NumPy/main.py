import numpy as np

# одномірний масив
# myArray = np.array([23,45,1,34,-5,23])
# print(myArray)

# Багатомірний масив
# testMatrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(testMatrix)

# Нульовий масив, заповняється нулями
# zeros = np.zeros((3,3)) # матриця 3х3
# print(zeros)

# Одиничний масив
# ones = np.ones((3,2))
# print(ones)

# Масив із множити значень
# Значення від 0 до 20 крок 3
# arr = np.arange(0,24,3)
# print(arr)

# Матриця у якої
# myarray = np.eye(3)
# print(myarray)

# Розмір 3х4 - значення випадкові від 0 до 1
# myrandom = np.random.rand(3,4)
# print(myrandom)

# Одноміний масив - рандом від 0,1
# myNumPy = np.random.rand(3)
# print(myNumPy)

#10 не включається
# myRandMinMax = np.random.randint(low=0, high=10, size=5)
# print(myRandMinMax)

# Не звичайні масиви
# myArray = np.array([[2,5,'Сало'], [3,3,False]])
# print(myArray)

# Розмір масиву
# print(f"Розмір масиву {myArray.shape}")
# print(f"Виміри масиву {myArray.ndim}") # Двох мірний масив
# print(f"Тип даних масиву {myArray.dtype}")
# print(f"Кількість елементів масиву {myArray.size}")

# Отримання елементів із масиву
# myList = np.array([23,12,4,6,23,9,-5,14,18])
# print("Перший елемента", myList[0])
# print("Зріз 1:4", myList[1:4]) # index 1 до index 3
# print("Зріз від початку :3", myList[:3]) # від початку 3 елемента
# print("Зріз від заданого і до кінця 2:", myList[2:]) # від 2 ідекса до кінця
# print("Обираємо кожен вказаний ::2", myList[::2]) # Кожен другий елемент
# print("Обираємо кожен вказаний 4::2", myList[4::2]) #
# print("Зріз від 2 ідекса до 7 ідекса 2:7:2 пригаємо через 2", myList[2:7:2]) #

# Обробка двох вимірних матриць
# matrix = np.array([[1, 9, 0], [4, -2, 6], [7, 16, 9]])
# print(matrix)
# # Зріз матриці
# print("2d array  [1:,:2]", matrix[1:,:2])

# Операції над масивами
a = np.array([2,5,-2,45,12,78,3,56])
b = np.array([-1,4,9,3,-9,12,3,-7])

items = np.linspace(0,1,12)
print("linspace ", items)

print("a: ", a)
print("b: ", b)
print("a+b: ", a+b)
print("a-b: ", a-b)
print("a*b: ", a*b)
print("a/b: ", a/b)
print("a//b: ", a//b)
print("a//b: ", a//b)
print("a % b:", a % b)
# print("a ** b:", a ** b)
print("a == b:", a == b)
print("a != b:", a != b)

# Статичтині методи у python
data = np.array([2,3,4,9,2,5,5,6,7,8])
print("data", data)
print("mean", np.mean(data)) #середнє арифметичне
print("median", np.median(data)) # медіана - середнє значення, більш точне
print("max", np.max(data)) # максимальне значення
print("min", np.min(data)) # мінімальне значення
