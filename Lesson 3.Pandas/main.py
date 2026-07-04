import numpy as np
import pandas as pd

print("-----------Pandas Working-----------")
items = pd.Series([23,56,2,4,6,1,'a'])
print(items)

print("items[2]", items[2])

item_index = pd.Series([18,16,21],
                       index=['Іванка','Мальвіна','Сара'])
print("Series - index")
print(item_index)

dictionary = pd.Series({"Матвій": 19, "Марко": 21})
print("Dictionary - index")
print(dictionary)

# DateFrame - табличка - двохмірний масив
df = pd.DataFrame({
    'Ім\'я': ['Анна', 'Богдан', 'Вікторія'],
    'Вік': [25,30,20],
    'Місто': ['Луцьк','Рівне','Тернопіль']
})
print("DataFrame - index")
print(df)

# Запис і читання csv - файлу
df.to_csv('data.csv', index=False)
print("DataFrame - columns")
print(df.columns)

my_reader = pd.read_csv('data.csv', encoding='utf8')
print("------Read DateFrame---------")
print(my_reader)

# Запис даних у Excel та читання
df.to_excel('friends.xlsx',sheet_name='Дівчата', index=False)

read_excel = pd.read_excel('friends.xlsx')
print("-----Read Excel------")
print(read_excel)

# Вивести дані у БД
import sqlite3

conn = sqlite3.connect('friends.db')
df.to_sql('friends', con=conn, if_exists='replace', index=False)

np.random.seed(42) # Ініціалізація рандому

df = pd.DataFrame({
    'Відділ': np.random.choice(['HR','IT','Sales'], size=100),
    'Зарплата': np.random.randint(3000, 8000, size=100),
    'Стаж': np.random.randint(1,20, size=100)
})

print("Перші 5 рядків:")
print(df.head())

# Статистика по даним
print("\n Статистика:")
print(df.describe())
# count (кількість)
# mean (середнє)
# std (стандартне відхилення)
# min (мінімум)
# 25% (перший квартиль)
# 50% (медіана)
# 75% (третій квартиль)
# max (максимум)

print("\nЗагальна інформація:")
print(df.info())

print("\nВпадкові значення - 3 штуки:")
print(df.sample(3))

# Групування і аналіз
print("\nСередня зарплата по відділах:")
print(df.groupby("Відділ")['Зарплата'].mean())