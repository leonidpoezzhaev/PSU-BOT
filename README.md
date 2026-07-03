# PSU-BOT

![Python](https://img.shields.io/badge/Python-3.14-007ec6?logo=python&logoColor=white)
![asyncio](https://img.shields.io/badge/Asyncio-3.14-007ec6?logo=python&logoColor=white)
![aiogram](https://img.shields.io/badge/Aiogram-3.25.0-007ec6?logo=telegram&logoColor=white)
![aiosqlite](https://img.shields.io/badge/Aiosqlite-0.22.1-007ec6?logo=sqlite&logoColor=white)
![icalendar](https://img.shields.io/badge/iCalendar-6.3.2-007ec6?logo=icalendar&logoColor=white)
![qrcode](https://img.shields.io/badge/QRcode-8.2-007ec6?logo=qrcode&logoColor=white)
![pandas](https://img.shields.io/badge/Pandas-3.0.2-007ec6?logo=pandas&logoColor=white)
![matplotlib](https://img.shields.io/badge/Matplotlib-3.10.7-007ec6?logo=matplotlib&logoColor=white)

Студенческий Telegram-бот для комфортного обучения в ПГНИУ (Пермский государственный национальный исследовательский университет).

**Бот доступен по ссылке:** [@PSUstudent_bot](https://t.me/PSUstudent_bot)

## 📌 Возможности

- **📅 Расписание** — просмотр актуального расписания прямо в чате. Бот подгружает данные из iCal-календаря, который можно синхронизировать с личным кабинетом на [student.psu.ru](https://student.psu.ru).
- **🔗 Сокращение ссылок** — быстро сокращайте длинные URL-адреса.
- **📱 Генерация QR-кодов** — создавайте QR-коды по ссылке или тексту.
- **🗺️ Карта университета** — быстрый доступ к карте кампуса.
- **ℹ️ Информация о боте** — краткое описание возможностей и инструкция по использованию.
- **🌐 Мультиязычность** — поддержка русского, английского и китайского языков.
- **📊 Статистика** — отслеживание активности пользователей и генерация диаграмм.

## 🚀 Установка и запуск

**1. Клонирование репозитория**

```bash
git clone https://github.com/leonidpoezzhaev/PSU-BOT.git
cd PSU-BOT
```

**2. Установка зависимостей**

```bash
pip install -r requirements.txt
```

Основные зависимости:
- `aiogram==3.25.0` — работа с Telegram Bot API
- `aiosqlite==0.22.1` — асинхронная работа с SQLite
- `icalendar==6.3.2` — парсинг iCal-расписания
- `qrcode==8.2` — генерация QR-кодов
- `pandas==3.0.2` и `matplotlib==3.10.7` — работа со статистикой

**3. Настройка**

Отредактируйте файл `config.py` и укажите:
- `TOKEN` — токен вашего Telegram-бота
- `ADMIN_CHAT` — ваш Telegram ID или ID чата для административных уведомлений

**4. Запуск**

```bash
python main.py
```

## 📁 Структура проекта

| Файл | Назначение |
|------|------------|
| `main.py` | Точка входа, инициализация бота и запуск polling |
| `handlers.py` | Основные обработчики команд и callback-запросов |
| `keyboards.py` | Клавиатуры для интерфейса бота |
| `config.py` | Конфигурация (токен, язык, текстовые сообщения) |
| `states.py` | FSM-состояния для диалогов с пользователем |
| `statistics.py` | Сбор и визуализация статистики |
| `urls.py` | Работа с iCal-ссылками и сокращение URL |
| `psu.db` | SQLite-база данных для хранения пользователей и их настроек |
| `requirements.txt` | Список зависимостей |

## 💡 Как пользоваться

1. **Запустите бота** командой `/start`.
2. **Выберите язык** — русский, английский или китайский.
3. **Добавьте ссылку на расписание** (iCal) — её можно скопировать в личном кабинете на [student.psu.ru](https://student.psu.ru).
4. **Используйте кнопки меню**:
   - «Моё расписание» — просмотр занятий на текущую неделю
   - «Сократить ссылку» — получение короткого URL
   - «Сгенерировать QR-код» — создание QR-кода по ссылке или тексту
   - «Карта университета» — просмотр карты кампуса
   - «О боте» — информация о возможностях
   - «Настройки» - настройки языка и ссылки

## 🛠️ Технологии

- **Python 3.x** — язык программирования
- **aiogram** — асинхронный фреймворк для Telegram Bot API
- **SQLite** — лёгкая реляционная база данных
- **iCalendar** — формат для работы с календарным расписанием
- **QRCode** — библиотека для генерации QR-кодов
