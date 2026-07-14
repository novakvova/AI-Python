import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, root_mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Отримуємо набір тестових даних із Каліфораній житло - 1990
# as_frame - дані будуть у вигляді DataFrame
hosing = fetch_california_housing(as_frame=True)

# Отримали дані у вигляду DataFrane
df = hosing.frame

print(df.head()) # виводимо 5 рядків, якщо без head() - консоль просто впаде

# Обираємо ознаки для множиної регресії

df = df[[
    "MedInc", # середній дохід наслення району
    "HouseAge", # середній вік будинку в районі
    "AveRooms",  # середня кількість кімнат будинку
    "MedHouseVal" # медіана вартості будинку - по суті це вартість буднику - цільова змінна
]]

# Створюємо категоріальні ознаки
# Буде доданий новий стовпчик у таблицю для категорій
df["Category"] = np.where(df["HouseAge"] > 30, "Old", "New")

print("Нова таблиця із категоріями")
print(df.head())

# Наводимо порядок Отримуємо список ознак без цільової ознаки
# X набір колонок без колонки MedHouseVal
X = df.drop(columns="MedHouseVal") # Сам df він не змінюється лише вертає колонку MedHouseVal

# print("x = ")
# print(X.head())
# Y - цільові ознаки для навчання моделі. Тобто tain
y = df["MedHouseVal"]
# print("y")
# print(y.head())

# Розподіл даних і налаштовуємо random
# X - Список ознак по яких будемо робити аналіз - експертизу
# y - Значення, яке потрібно прогозувати - цільова ознака
# test_size - 20% це будуть дані для тесту
# 80% - це для навчання - виявлення закономірносте даних
# random_state=42 - для того, щоб дані завжди були однаковими
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Робимо попердню обробку даних
numeric_features = [
    "MedInc",
    "HouseAge",
    "AveRooms"
]

categorical_features = [
    "Category"
]

preprocessor = ColumnTransformer(
    # Правила для обробки інформації
    transformers=[
        (
            # Назва трансформації
            "num",
            #Буде усі числові конки приводити до значення - близького до 1
            #Віднімаємо середнє і ділимо на стандартне відхилення
            StandardScaler(),
            # Це будемо робити на основі ось цих даниї
            numeric_features
        ),
        (
            "cat",
            # воно приводити дані до числоваого формату
            # при цьому буде лише 1 колонка у які буде вказано 0 або 1
            OneHotEncoder(drop='first'),
            categorical_features # Застосовуємо до цих даних
        )
    ]
)

# Робимо конвеєр обробки даних
model = Pipeline([
    (
        # назва 1 етапу
        "preprocessor",
        # Попередня обробка даних: Стандартизація та Кодування Категоріальних ознак
        preprocessor
    ),
    (
        "regressor", # Назва 2 етапу
        LinearRegression() # Множина лінійна регресія
    )
])

# Модель уже знає як працювати із даними, ми передали і вказали усі парамери
# проводимо машине навчання
model.fit(X_train, y_train) # Якщо провели машинне навчання, можна робити передбачення

y_pred = model.predict(X_test) # Отриуємо масив прогнозів на основі тестових даних

# print(y_pred[:5])

# Оцінка моделі
# передаємо отримані дані і тестові дані, які у нас вийшли
r2 = r2_score(y_test, y_pred)  # Коефіцієнт детермінації

# шукаємо абсолютну похибку
mae = mean_absolute_error(y_test, y_pred)

# Середньо квадратична похибка даних
rmse = root_mean_squared_error(y_test, y_pred)

print("r2 score: ", r2)
print("mae score: ", mae) # похибка очислень - 0.6 - якщо будинок коштує сотні тисяч - то похибка 60 тисяч
print("rmse: ", rmse) # Дана змінна реагує на досить великі відхилення від норми

# ==========================================
# 11. Коефіцієнти моделі
# ==========================================
# Формуємо список назв усіх ознак,
# які були використані моделлю після попередньої обробки.
feature_names = (
    # Додаємо числові ознаки.
    numeric_features +
    # Додаємо назви нових стовпців,
    # створених OneHotEncoder.
    list(
        # Отримуємо об'єкт попередньої обробки (ColumnTransformer)
        # із Pipeline.
        model.named_steps["preprocessor"]
                # Отримуємо трансформатор категоріальних ознак.
             .named_transformers_["cat"]
# Повертаємо назви стовпців після OneHotEncoder.
             # Наприклад:
             # Category → Category_New
             .get_feature_names_out(categorical_features)
    )
)
# Отримуємо коефіцієнти навченої моделі
# множинної лінійної регресії.
coef = model.named_steps["regressor"].coef_

# Створюємо DataFrame,
# у якому кожній ознаці відповідає її коефіцієнт.
coef_df = pd.DataFrame({
    "Feature": feature_names,
    "Coefficient": coef
})
# Виводимо заголовок.
print("\nКоефіцієнти моделі:")
# Виводимо таблицю коефіцієнтів.
print(coef_df)

# Ознака	Коефіцієнт	        Інтерпретація
# MedInc	    0.848	    Найбільший позитивний вплив на прогнозовану вартість будинку.
# HouseAge	    0.294	    Старіші будинки, як правило, мають вищу прогнозовану вартість.
# AveRooms	    −0.067	    Незначний негативний вплив. За інших однакових умов збільшення середньої кількості кімнат трохи зменшує прогнозовану ціну.
# Category_Old	−0.197	    Будинки категорії Old мають нижчу прогнозовану вартість порівняно з базовою категорією (New)

