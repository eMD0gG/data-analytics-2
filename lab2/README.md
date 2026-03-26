# Анализ комментариев к трейлерам фильмов с помощью GigaChat

## Описание

Python-скрипт анализирует комментарии к трейлерам фильмов через GigaChat API и определяет тональность, эмоции и другие параметры.

## Структура проекта

```
.
├── config.py             # Настройки (ключ API, промпт, папка для входных и выходных данных)
├── llm_api.py            # Вызов GigaChat
├── main.py               # Основной скрипт
├── input_data/           # Папка с входными CSV
└── output_data/          # Папка с результатами
```

## Инструкция запуска

### 1. Установите библиотеку

```bash
pip install gigachat
```

### 2. Получите ключ API

Зарегистрируйтесь на [developers.sber.ru](https://developers.sber.ru/portal/products/gigachat-api) и получите ключ авторизации GigaChat.

### 3. Настройте ключ

В файле `config.py` замените `"YourAuthorizationKey"` на ваш ключ:

```python
GIGACHAT_CREDENTIALS = "ваш_ключ_здесь"
```

### 4. Подготовьте данные

Положите CSV-файл с комментариями в папку `input_data/`.  
Файл должен содержать колонки: `comment_id`, `video_title`, `processed_comment`.

### 5. Запустите скрипт

```bash
python main.py
```

Введите номер файла из списка и нажмите Enter.

### 6. Получите результат

Результат появится в папке `output_data/` с суффиксом `_output.csv`.

## Параметры анализа

| Параметр | Описание |
|----------|----------|
| **sentiment** | Общая тональность комментария по отношению к трейлеру или будущему фильму |
| **emotion** | Основная эмоция, выраженная в комментарии. Для трейлеров характерна эмоция `anticipation` (ожидание) |
| **intensity** | Сила проявления эмоции. Число от 1 до 10, где 1–3 — слабо выражено, 4–7 — умеренно, 8–10 — очень сильно |
| **aspects** | Аспекты фильма, которые упоминаются в комментарии: `acting` (актёрская игра), `plot` (сюжет), `visuals` (визуальные эффекты), `music` (музыка), `direction` (режиссура), `characters` (персонажи), `pacing` (темп), `dialogue` (диалоги). Если аспекты не упомянуты — пустой список |
| **recommendation** | Намерение автора комментария посмотреть фильм в кинотеатре или онлайн |


## Пример входных данных

`input_data/comments.csv`:

```csv
comment_id,video_title,processed_comment
1,Avengers Endgame Trailer,peak marvel
2,Avengers Endgame Trailer,worst movie mcu
```

## Пример выходных данных

`output_data/comments_output.csv`:

```csv
comment_id,video_title,comment,sentiment,emotion,intensity,aspects,recommendation
1,Avengers Endgame Trailer,peak marvel,positive,joy,9,,True
2,Avengers Endgame Trailer,worst movie mcu,negative,disgust,9,,False
```