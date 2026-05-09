# Мини-продукт с LLM-аналитикой


## Ссылка на проект

Опробовать проект можно по ссылке: https://data-analytics-2-lab3.streamlit.app/

## Описание

Проект представляет собой Streamlit страницу, где можно загрузить датасет и по запросу получить необходимые метрики.

## Инструкция по запуску

**Установка зависимостей:**
```
pip install -r requirements.txt
```

---

**Регистрация и получение API ключа:**
1) Перейдите на groq:
https://groq.com/
2) Зарегистрируйтесь или войдите в аккаунт
3) Откройте раздел `API Keys`
4) Нажмите `Create API Key`, выберите имя и дату истечения ключа
5) Скопируйте полученный ключ

---

**Создание файла secrets.toml:**

В корневой папке проекта создайте папку `.streamlit`, а в ней файл `secrets.toml` со следующим содержанием:
```
GROQ_API_KEY = "YOUR_API_KEY"
```
Вставьте ваш скопированный ключ вместо YOUR_API_KEY

---

**Запуск скрипта:**

В терминале выполните команду:

```
streamlit run app.py
```

## Пример работы

**Входные данные:** 
Для примера был взят датасет: [Rainfall Prediction using Machine Learning](https://www.kaggle.com/datasets/subho117/rainfall-prediction-using-machine-learning).

**Выходные данные:**

![Ответ модели](.\assets\Screenshot1.png)
![Ответ модели](.\assets\Screenshot2.png)